import psycopg2

# Подключаемся к дефолтной БД postgres чтобы создать новую
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="test",
    database="postgres"
)
conn.autocommit = True  # для CREATE DATABASE нужен autocommit
cur = conn.cursor()

# Удаляем БД testdb если существует, и создаём заново
cur.execute("DROP DATABASE IF EXISTS testdb")
cur.execute("CREATE DATABASE testdb")
print("База testdb создана")

cur.close()
conn.close()

# Подключаемся к новой БД testdb и создаём таблицы
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="test",
    database="testdb"
)
cur = conn.cursor()

# === Создаём таблицы ===

cur.execute("""
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        created_at DATE DEFAULT CURRENT_DATE
    )
""")

cur.execute("""
    CREATE TABLE products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2) NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE orders (
        id SERIAL PRIMARY KEY,
        user_id INT REFERENCES users(id),
        product_id INT REFERENCES products(id),
        amount DECIMAL(10, 2) NOT NULL,
        status VARCHAR(20) NOT NULL,
        created_at DATE DEFAULT CURRENT_DATE
    )
""")

print("Таблицы созданы")

# === Заполняем данными ===

cur.execute("""
    INSERT INTO users (name, email, created_at) VALUES
        ('Anna',   'anna@test.com',   '2024-01-15'),
        ('Boris',  'boris@test.com',  '2024-02-20'),
        ('Carol',  'carol@test.com',  '2024-03-10'),
        ('Dmitry', 'dmitry@test.com', '2024-04-05'),
        ('Elena',  'elena@test.com',  '2024-05-12')
""")

cur.execute("""
    INSERT INTO products (name, price) VALUES
        ('Laptop',     1200.00),
        ('Phone',       800.00),
        ('Headphones',  150.00),
        ('Keyboard',     80.00),
        ('Monitor',     350.00)
""")

cur.execute("""
    INSERT INTO orders (user_id, product_id, amount, status, created_at) VALUES
        (1, 1, 1200.00, 'paid',     '2024-02-01'),
        (1, 3,  150.00, 'paid',     '2024-02-15'),
        (1, 4,   80.00, 'shipped',  '2024-03-01'),
        (2, 2,  800.00, 'paid',     '2024-03-10'),
        (2, 5,  350.00, 'pending',  '2024-04-20'),
        (3, 1, 1200.00, 'cancelled','2024-04-25'),
        (3, 3,  150.00, 'paid',     '2024-05-05'),
        (4, 2,  800.00, 'paid',     '2024-05-15'),
        (4, 4,   80.00, 'paid',     '2024-05-20'),
        (4, 5,  350.00, 'shipped',  '2024-06-01')
""")

conn.commit()
print("Данные вставлены")

# === Проверка ===

cur.execute("SELECT COUNT(*) FROM users")
print(f"Пользователей: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM products")
print(f"Продуктов: {cur.fetchone()[0]}")

cur.execute("SELECT COUNT(*) FROM orders")
print(f"Заказов: {cur.fetchone()[0]}")

cur.close()
conn.close()
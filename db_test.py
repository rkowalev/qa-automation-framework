import psycopg2

# Параметры подключения
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="test",
    database="postgres"  # дефолтная БД, которая создаётся при старте
)

# Создаём cursor — объект через который выполняются запросы
cur = conn.cursor()

# Выполняем простейший запрос
cur.execute("SELECT 1")

# Получаем результат
result = cur.fetchone()
print(result)  # → (1,)

# Закрываем
cur.close()
conn.close()

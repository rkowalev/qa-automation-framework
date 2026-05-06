import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="test",
    database="testdb"  # подключаемся к нашей тестовой БД
)
cur = conn.cursor()

# Сюда будем писать SQL и смотреть результаты
query = """
    SELECT * FROM 
"""

cur.execute(query)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
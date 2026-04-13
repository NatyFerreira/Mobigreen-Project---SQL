import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="mobigreen_urban",
    user="admin",
    password="admin_pass"   # coloque sua senha real
)

cursor = conn.cursor()

email = "alice@example.com"

cursor.execute("SELECT * FROM usagers WHERE email = %s", (email,))
rows = cursor.fetchall()
print(rows)

cursor.close()
conn.close()

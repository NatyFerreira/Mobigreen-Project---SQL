import psycopg2

conn = psycopg2.connect(
    host="127.0.0.1",
    port=5432,
    database="mobigreen_urban",
    user="admin",
    password="admin"
)

cursor = conn.cursor()

# Mesmo ataque
nom = "' OR '1'='1"

# Consulta segura (prepared statement)
query = "SELECT * FROM usagers WHERE nom = %s;"
print("Consulta executada:", query)

cursor.execute(query, (nom,))
rows = cursor.fetchall()

print("Resultado com prepared statement:")
for row in rows:
    print(row)

cursor.close()
conn.close()


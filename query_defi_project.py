import psycopg2

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="defi_project",
    user="postgres",
    password="LiA86k:)",  # Replace with your actual password
    host="localhost",
    port="5432"
)

# Create a cursor
cur = conn.cursor()

# Query the database
cur.execute("SELECT * FROM defi_data;")

# Fetch and print results
rows = cur.fetchall()
for row in rows:
    print(row)

# Close connections
cur.close()
conn.close()

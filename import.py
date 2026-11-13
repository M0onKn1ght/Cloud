import psycopg2

# Twój link z wymuszonym SSL
db_url = "postgresql://wsbmerito:vUbWwfBZgIxUNxi3QJrWXkN5eT99Iwcm@dpg-dbrbmo0ae00c73f6nhd0-a.frankfurt-postgres.render.com/postgres123_933u?sslmode=require"

print("Łączenie z bazą...")
conn = psycopg2.connect(db_url)
cursor = conn.cursor()

# Tworzenie tabeli
cursor.execute("CREATE TABLE IF NOT EXISTS pizza (id SERIAL PRIMARY KEY, name VARCHAR(50) NOT NULL, description VARCHAR(200) NOT NULL, price FLOAT NOT NULL);")

# Dodanie testowej pizzy
cursor.execute("INSERT INTO pizza (name, description, price) VALUES ('Margherita', 'Tomato sauce, mozzarella cheese, fresh basil', 25.0);")

conn.commit()
cursor.close()
conn.close()

print("Sukces! Tabela została utworzona, a pizza dodana do bazy.")
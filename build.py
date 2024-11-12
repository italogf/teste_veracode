import sqlite3

def create_database():

    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()


    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL
    )
    ''')

    # Insere alguns dados de exemplo
    cursor.execute("INSERT INTO users (username) VALUES ('admin')")
    cursor.execute("INSERT INTO users (username) VALUES ('user1')")
    cursor.execute("INSERT INTO users (username) VALUES ('user2')")
    cursor.execute("INSERT INTO users (username) VALUES ('test')")    
    cursor.execute("INSERT INTO users (username) VALUES ('user2')")
    cursor.execute("INSERT INTO users (username) VALUES ('test3')")
    cursor.execute("INSERT INTO users (username) VALUES ('user21')")
    cursor.execute("INSERT INTO users (username) VALUES ('test4')")
    cursor.execute("INSERT INTO users (username) VALUES ('user5')")
    cursor.execute("INSERT INTO users (username) VALUES ('test39')")

    # Salva (commit) as mudanças
    connection.commit()

    # Fecha a conexão
    connection.close()

# Cria o banco de dados e a tabela
create_database()
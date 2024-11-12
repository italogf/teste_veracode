import sqlite3

def create_database():
    # Conecta ao banco de dados (ou cria um novo)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Cria a tabela 'users' com duas colunas: id e username
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

    # Salva (commit) as mudanças
    connection.commit()

    # Fecha a conexão
    connection.close()

# Cria o banco de dados e a tabela
create_database()
import sqlite3

def get_user_data(username):
    # Conecta ao banco de dados (exemplo com SQLite)
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()

    # Consulta usando parâmetros para evitar SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)

    # Recupera os resultados
    result = cursor.fetchall()

    # Fecha a conexão
    connection.close()

    return result

# Solicita o nome de usuário ao usuário
user_input = input("Enter your username: ")

# Executa a consulta de forma segura
user_data = get_user_data(user_input)

# Exibe os dados do usuário
print(user_data)

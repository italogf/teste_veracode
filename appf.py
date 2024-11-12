from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape
import sqlite3

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

senha_armazenada = "senha_secreta"

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Rota de login
@app.route('/login', methods=['POST'])
def login():
    usuario = escape(request.form['usuario'])
    senha = escape(request.form['senha'])

    # Verificar a senha de forma segura (não seguro, apenas para fins de demonstração)
    if senha == senha_armazenada:
        session['usuario'] = usuario
        return redirect(url_for('dashboard'))
    else:
        return "Credenciais inválidas. Tente novamente."

# Rota do dashboard
@app.route('/dashboard')
def dashboard():
    if 'usuario' in session:
        return f"Bem-vindo, {escape(session['usuario'])}! Esta é a sua área segura."
    else:
        return redirect(url_for('index'))

# Rota de logout
@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('index'))

# Rota para simular SQL Injection, acessível apenas para usuários autenticados
@app.route('/users', methods=['GET', 'POST'])
def users():
    if 'usuario' not in session:
        return redirect(url_for('index'))

    if request.method == 'POST':
        user_input = request.form['username']
        users_data = get_user_data(user_input)
        return render_template('users.html', users=users_data)
    
    return render_template('users.html', users=None)

# Função vulnerável a SQL Injection
def get_user_data(username):
    # Conecta ao banco de dados (exemplo com SQLite)
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()

    # Consulta vulnerável a SQL Injection
    query = "SELECT * FROM users WHERE username = '" + username + "';"
    cursor.execute(query)

    # Recupera os resultados
    result = cursor.fetchall()

    # Fecha a conexão
    connection.close()

    return result

if __name__ == '__main__':
    app.run(debug=True)

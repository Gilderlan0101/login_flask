from flask import Flask, render_template, request

app = Flask(__name__)

def usuario():
    # Dicionário de usuários com emails e senhas
    users = {'lansilva@gmail.com': '1234'}
    return users

@app.route('/')
def home():
    # Renderizando uma pagina http 
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Request.form -> para receber dados de um fomulario vindo do cliente
    name = request.form.get('nome')
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Obtém o dicionário de usuários
    users = usuario()
    
    # Verifica se o email está no dicionário e se a senha corresponde
    if email in users and users[email] == senha:
        return render_template('pefil.html', name=name)
    else:
        
        return "Login falhou, tente novamente!"

if __name__ == '__main__':
    app.run(debug=True)

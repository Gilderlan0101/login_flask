Dois metodos comus são (GET e POST)  (GET) mas comum em procura algum produto no site ou pefil já que quando usamos o método get as informaçoes pesquisadas vão aparece na barra de 
pesquisa
Oque não seria certo em uma tela de login, Não e seguro então usamos o metodo post
O metodo (POST) é  ao contrario do get, ele vai esconde as informaçoes da barra de pesquisa mas ainda sim e posivel visualiza na requisição
Para melhora a segurança do site devemos usar (HTTPS) criptografa os dados trasmitidos, protejento contra ataques. [ não foi usado neste projeto] apenas uma dica.

Também é possível receber dados vindo do cliente e tratá-los como deseja:
primeiro importamos o modolo  request no flask

    from flask import Flask, render_template, request

Lembramos que no HTML devemos passar requered nos inputs junto a um nome para poder usar

no flask da seguinte forma:
    <div class="login">
        <form action="login" method="post">
            <label for="email">Email</label>
            <input type="text" id="email" name="email" placeholder="Digite seu email." required>
            <br><br>
            <label for="senha">Senha</label>
            <input type="password" id="senha", name="senha" placeholder="Digite sua senha."required>
            
            <br><br>
            <button type="submit" id="Enviar">Enviar</button>
            
        </form>
    </div>


Feito isso, já podemos fazer nossa lógica


    @app.route('/login', methods=['POST'])
def login():
    # Request.form -> para receber dados de um fomulario vindo do cliente
    email = request.form.get('email')
    senha = request.form.get('senha')

    # Obtém o dicionário de usuários
    users = usuario()

    # Verifica se o email está no dicionário e se a senha corresponde
    if email in users and users[email] == senha:
        return render_template('pefil.html')
    else:
        users.append(email, senha)
        return "Login falhou, tente novamente!"


Veja que nesta parte passamos o request.form.get. Ele vai pegar os dados que serão passados para os inputs que vêm do cliente e envia para o provedor que vai tratar esses dados.
 email = request.form.get('email')
 senha = request.form.get('senha')

 

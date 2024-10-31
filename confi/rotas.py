from flask import Flask, render_template, request, url_for, redirect, session
from dotenv import load_dotenv
import os
import confi as cf

app = Flask(__name__, template_folder='../templates')
app.secret_key = os.getenv('SECRET_KEY')

@app.template_filter('nl2br')
def nl2br_filter(s):
    return s.replace('\n', '<br>')

#rota da pagina
@app.route('/')
def inicio():
    return render_template('index.html', palavra_secreta=cf.palavra_secreta_jogo, letra_enviada=' ')

#rota do btn ENTER
@app.route('/submit', methods=['POST'])
def submit():
    letra = request.form['letra']
    erros = request['mensagem_feedback']

    if letra in cf.palavra_secreta_jogo:
        #quando acerta a letra
        session['letras_enviadas'] = session.get('letras_enviadas', []) + [letra]
        return redirect(url_for('index'))
    else:
        #mensagem para o erro
        return render_template('index.html', erros= 'Letra incorreta')

if __name__ == '__main__':
    app.run(debug=True)
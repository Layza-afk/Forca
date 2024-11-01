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
    session['tentativas'] = 6
    session['letra_input'] = []
    return render_template('index.html', palavra_secreta=cf.palavra_secreta_jogo, letra_input=[])

#rota do btn ENTER
@app.route('/submit', methods=['POST'])
def submit():
    letra = request.form['letra']
    session['letra_input'] = session.get('letra_input', [''])

    #AHHHHHH CONSEGUI!!!!!!!!!!!! Esse if cuida de exbir as letrasjá digitadas pelo user
    if letra not in cf.palavra_secreta_jogo or letra in cf.palavra_secreta_jogo:
        session['letra_input'].append(letra)
        
    if letra not in cf.palavra_secreta_jogo:
        session['tentativas'] -= 1

    # Atualiza a palavra exibida com base nas letras enviadas
    palavra_exibida = cf.atualizar_palavra_exibida(session['letra_input'])
    return render_template(
        'index.html', 
        palavra_secreta=palavra_exibida, 
        letra_input=session['letra_input'],
        tentativas=session['tentativas']
        )

if __name__ == '__main__':
    app.run(debug=True)
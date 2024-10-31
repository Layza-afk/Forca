import random
import rotas as rt

palavras_aleatorias = ['letra', 'telhado', 'gato', 'sogra', 'geladeira', 'jujuba', 'taxa', 'balde', 'lhama', 'letal']

palavra_secreta_jogo = random.choice(palavras_aleatorias)
contagem = 0
def verificar():
    for i in palavras_aleatorias:
        contagem += 1
import random
palavras_aleatorias = ['letra', 'telhado', 'gato', 'sogra', 'geladeira', 'jujuba', 'taxa', 'balde', 'lhama', 'letal']

palavra_secreta_jogo = random.choice(palavras_aleatorias)

def atualizar_palavra_exibida(letras_enviadas):
    #Retorna a palavra com letras acertadas e '_' para as não reveladas
    nova_palavra = ""
    for letra in palavra_secreta_jogo:
        if letra in letras_enviadas:
            nova_palavra += letra
        else:
            nova_palavra += "_"
    return nova_palavra
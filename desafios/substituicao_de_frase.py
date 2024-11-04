import re

def substituicao_de_frase(texto):
    padrao = r'not .*? bad'

    nova_frase = re.sub(padrao, 'good', texto)

    print(nova_frase)


if __name__ == '__main__':
    substituicao_de_frase('the food is not so bad')

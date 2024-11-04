row = 'vinicius', 'MD', 22, 1.75

def pessoa(tupla):
    # nome, cidade, idade, altura = tupla
    # nome, idade = tupla[0], tupla[-2]
    (nome, *_, altura) = tupla
    print(nome, altura, *_)

# pessoa(row)

tabela = (('vinicius', 22),
          ('joao', 25)
          )

for nome, idade in tabela:
    print(nome, idade)
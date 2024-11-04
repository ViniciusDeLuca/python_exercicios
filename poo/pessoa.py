class Pessoa:
    genero = 'masculino'
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class PessoaMasculino(Pessoa):
    def __init__(self, altura):
        super().__init__('vinicius', 22)
        self.altura = altura

p = PessoaMasculino(1.8)
print(p.nome)
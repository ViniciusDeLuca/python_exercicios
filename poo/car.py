class Car:
    nome = 'ferrari'
    def __init__(self, modelo):
        self.modelo = modelo
        self.motor_ligado = False
    def ignicao(self):
        self.motor_ligado = True
        print('vrum...')

c = Car('F50')
c.ignicao()
print(c.nome, c.modelo, c.motor_ligado)
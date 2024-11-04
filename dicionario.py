d = {'cidade': 'Maceio', 'estado': 'AL'}

# print(d.get('cidade'))
# print('cidade' in d)
# print('Al' in d.values())
#
# print(d.items())

a = [
    d,
    {'cidade': 'Recife', 'estado': 'PE'},
]
# print(a[0])
#para deletar algo dentro do dicionario, usa-se del

d.update(interesses=['autonomia', 'hack'])
d.pop('interesses') #para remover
print(d)
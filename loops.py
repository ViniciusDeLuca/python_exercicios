nome = 'vinicius'

print(nome, len(nome))

i = 0

# for i in range(0,len(nome), 2):
#     print(nome[i])

# while i < len(nome):
#     print(nome[i])
#     i += 1

# for i in enumerate(nome):
#     print(i)

#para pular um passo:
for i, j in enumerate(nome):
    if j == 'i':
        continue
    print(i, j)

#para parar iteração:
for i, j in enumerate(nome):
    if j == 'i':
        break
    print(i, j)

# print(list(range(1,50, 10))) # incio, fim, passo
from re import match, findall

#para buscar especificamente 5 repeticoes da string literal citada
print(match(r'\w{5}', 'abcsd'))

# para pelo menos a quantidade minima
print(match(r'\w{2,}', 'abcsd'))

# mas para buscar somente a quantidade minima, acrescento o ?
print(match(r'\w{2,}?', 'abcsd'))

# posso definir o minimo e o maximo
print(match(r'\w{2,5}', 'abcsd'))

# 0 ou 1 ocorrencia tem algumas variacoes
match(r'\w{0,1}', 'abcsd')
match(r'\w{,1}', 'abcsd')
match(r'\w{,1}?', 'abcsd')
match(r'\w??', 'abcsd')


# 0 ou mais ocorrencias

match(r'\w{0,}', 'asdadsaca')
match(r'\w{,}', 'asdadsaca')
match(r'\w*', 'asdadsaca')
match(r'\w*?', 'asdadsaca') #neste caso pega o minimo possivel


#1 ou mais ocorrencias
match(r'\w{1,}', 'asdadsaca')
match(r'\w+', 'asdadsaca')
match(r'\w+?', 'asdadsaca') #neste caso pega o minimo possivel

# caso onde a interrogacao faz diferenca e prova-se o uso

texto = 'attr1="value1" attr2="value2"'

print(findall(r'".+?"', texto))

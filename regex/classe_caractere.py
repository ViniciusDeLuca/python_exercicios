from re import findall

#para achar e retornar todas as ocorrencias dos caracteres do primeiro parametro
print(findall('[aeiou]', 'Vinicius de luca'))

#negacao do caso acima, entao retorna todos os caracteres nao presentes na lista citada
print(findall('[^aeiou]', 'Vinicius de luca'))

#encontrar o range citado
print(findall('[a-zA-Z0-9_]', 'Vinicius de luca 18'))

#mesma regex acima representada por '\w'
print(findall('[\w]', 'Vinicius de luca 18'))

#sequencias especiais

# \d - [0-9]
# \D - [^0-9]
# \s - [\t\n\r\f\v]
# \S - [^\t\n\r\f\v]
# \w - [a-zA-Z0-9_]
# \W - [^a-zA-Z0-9_]
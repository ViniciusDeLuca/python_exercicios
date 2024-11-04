import re

re.match('abc', 'abc')

#para achar o padrao em um texto
re.search('abc', '000abcdef')

#para achar o padrao (ocorrencia) ao longo de um texto
re.findall('abc', 'asd abc asdasd')

#metacaracter '.'
re.match('.', 'abc')

#ancoras '^' (para inicio) e '$' (para final)
print(re.findall('^.', 'abc\ndef'))
print(re.findall('.$', 'abc abc\ndefc'))


#flag multilinhas
print(re.findall('^.', 'abc\ndef', re.MULTILINE))
print(re.findall('.$', 'abc abc\ndefc',re.MULTILINE))




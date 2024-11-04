from re import match
#para usar condicao OR na regex, utilize |
# sempre retornará o da esquerda

print(match('a|b', 'afbc'))
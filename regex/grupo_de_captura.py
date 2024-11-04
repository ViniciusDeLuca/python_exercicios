from re import match

html = '<input type="text" name="nome" id="id_nome">'

# quando coloco em parenteses
pattern = r'<(.+?) type="(.+?)" name="(.+?)" id="(.+?)"'
m = match(pattern, html)
print(m.groups()) #retorna uma tupla com os valores dos grupos

# para retornar um grupo especifico
print(m.group(0, 2))

# grupos de nao captura (?:)

pattern_nao_agrupado = r'<(.+?) (?:(?:type="(.+?)"|name="(.+?)"|id="(.+?)") ?)*'

m_nao_agrupado = match(pattern_nao_agrupado, html)
print(m_nao_agrupado.groups())
#o primeiro (?:) é para os espaços opcionais, o segundo é para ordem e é aplicado junto do pipe (OR)

# named groups ?P<nome>
pattern_grupo_nomeado = r'<(?P<tag>.+?) (?:(?:type="(?P<type>.+?)"|name="(?P<name>.+?)"|id="(?P<id>.+?)") ?)*'

m2 = match(pattern_grupo_nomeado, html)
# retorna um dicionario com a chave do grupo e o valor
print(m2.groupdict())
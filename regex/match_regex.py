from re import match

m= match(r'\d+', '12345')

print(m.group(), m.start(), m.end(), m.span())
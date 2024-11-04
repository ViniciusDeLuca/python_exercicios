import math

def recortar_colar(a, b):
    metade_a = int(math.ceil(len(a)/2))

    metade_b = int(math.ceil(len(b)/2))

    palavra_conjunta = [a[:metade_a], b[:metade_b], a[metade_a:], b[metade_b:]]

    print(''.join(palavra_conjunta))

if __name__ == '__main__':
    recortar_colar('abcde', 'xyz')
    recortar_colar('Kitten', 'Donut')

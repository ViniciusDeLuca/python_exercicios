import math

def recortar_colar(a, b):
    metade_a = math.ceil(len(a)/2)

    metade_b = math.ceil(len(b)/2)

    print(metade_a, metade_b)

if __name__ == '__main__':
    recortar_colar('abcde', 'xyz')
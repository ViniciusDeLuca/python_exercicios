def mix(a, b):
    ultima_letra_palavra_um = a[0:2]
    ultima_letra_palavra_dois = b[0:2]

    nova_palavra_um = b.replace(ultima_letra_palavra_dois, ultima_letra_palavra_um)
    nova_palavra_dois = a.replace(ultima_letra_palavra_um, ultima_letra_palavra_dois)

    print(' '.join([nova_palavra_um, nova_palavra_dois]))

if __name__ == '__main__':
    mix('mix', 'pod')
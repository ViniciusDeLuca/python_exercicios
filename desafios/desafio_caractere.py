def substituicao_caractere(palavra):
    primeira_letra = palavra[0]
    # for i, c in enumerate(palavra):
    #     if c == primeira_letra and i != 0:
    #         print('*')
    #         continue
    #     print(c)
    nova_palavra = primeira_letra + palavra[1:].replace(primeira_letra, '*')
    print(nova_palavra)

substituicao_caractere('caractere')
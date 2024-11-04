def extremos(palavra):
    if len(palavra) < 2:
        print('')
        return
    print(palavra[0:2:1] + palavra[-2: len(palavra)])

extremos('v')
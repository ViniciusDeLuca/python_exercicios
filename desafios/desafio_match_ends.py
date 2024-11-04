def match_ends(a : list):
    # for i in a:
    #     if len(i) > 2 and i[0] == i[len(i)-1]:
    #         if len(lista_final) > 0 and len(i) > len(lista_final[0]):
    #             print(lista_final[0])
    #             lista_final = lista_final[0]
    #         else:
    #             lista_final.append(i)

    lista_final = (item for item in a if len(item) > 2 and item[0] == item[-1])
    print(max(len(item) for item in lista_final))

if __name__ == '__main__':
    match_ends(['aba', '', 'aa', 'helloh'])
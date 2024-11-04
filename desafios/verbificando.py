def verbificar(p):
    if len(p) < 3:
        print(p)
        return
    match p[-3:]:
        case 'ing':
            print(f"{p}ly")
        case _:
            print (f"{p}ing")

if __name__ == '__main__':
    verbificar('swing')
    verbificar('hail')
    verbificar('do')
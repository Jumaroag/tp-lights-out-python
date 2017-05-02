import tablero
tablero.tablero_1()
def traductor():
    print("¿Qué poscición deseas jugar?")
    a = input()
    a = str(a)
    a = a.lower()
    if (a in tablero.tablero_1()):
        print(tablero.tablero_1()[a])
    elif (a not in tablero.tablero_1()):
        print("Poscicion no valida, elija una poscición comprendida entre A1 y E5")
        traductor()

traductor()
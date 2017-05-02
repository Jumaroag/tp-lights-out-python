import tablero
tablero.posciciones_del_tablero()
def traductor():
    print("¿Qué poscición deseas jugar?")
    a = input()
    a = str(a)
    a = a.lower()
    if (a in tablero.posciciones_del_tablero()):
        print(tablero.posciciones_del_tablero()[a])
    elif (a not in tablero.posciciones_del_tablero()):
        print("Poscicion no valida, elija una poscición comprendida entre A1 y E5")
        traductor()

traductor()
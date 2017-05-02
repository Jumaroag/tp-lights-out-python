import tablero
tablero.posciciones_del_tablero()
def diccionario_a_formato_agradable():
    a = tablero.posciciones_del_tablero()["a1"] + " " + tablero.posciciones_del_tablero()["a2"] + " " + tablero.posciciones_del_tablero()["a3"] + " " + tablero.posciciones_del_tablero()["a4"] + " " + tablero.posciciones_del_tablero()["a5"]
    b = tablero.posciciones_del_tablero()["b1"] + " " + tablero.posciciones_del_tablero()["b2"] + " " + tablero.posciciones_del_tablero()["b3"] + " " + tablero.posciciones_del_tablero()["b4"] + " " + tablero.posciciones_del_tablero()["b5"]
    c = tablero.posciciones_del_tablero()["c1"] + " " + tablero.posciciones_del_tablero()["c2"] + " " + tablero.posciciones_del_tablero()["c3"] + " " + tablero.posciciones_del_tablero()["c4"] + " " + tablero.posciciones_del_tablero()["c5"]
    d = tablero.posciciones_del_tablero()["d1"] + " " + tablero.posciciones_del_tablero()["d2"] + " " + tablero.posciciones_del_tablero()["d3"] + " " + tablero.posciciones_del_tablero()["d4"] + " " + tablero.posciciones_del_tablero()["d5"]
    e = tablero.posciciones_del_tablero()["e1"] + " " + tablero.posciciones_del_tablero()["e2"] + " " + tablero.posciciones_del_tablero()["e3"] + " " + tablero.posciciones_del_tablero()["e4"] + " " + tablero.posciciones_del_tablero()["e5"]
    abcde = a, b, c, d, e
    print("   A B C D E")
    for n,x in enumerate(abcde):
        print(n+1,"|" + x)
diccionario_a_formato_agradable()
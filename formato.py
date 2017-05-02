import tablero
tablero.tablero_1()
def diccionario_a_formato_agradable():
    a = tablero.tablero_1()["a1"] + " " + tablero.tablero_1()["a2"] + " " + tablero.tablero_1()["a3"] + " " + tablero.tablero_1()["a4"] + " " + tablero.tablero_1()["a5"]
    b = tablero.tablero_1()["b1"] + " " + tablero.tablero_1()["b2"] + " " + tablero.tablero_1()["b3"] + " " + tablero.tablero_1()["b4"] + " " + tablero.tablero_1()["b5"]
    c = tablero.tablero_1()["c1"] + " " + tablero.tablero_1()["c2"] + " " + tablero.tablero_1()["c3"] + " " + tablero.tablero_1()["c4"] + " " + tablero.tablero_1()["c5"]
    d = tablero.tablero_1()["d1"] + " " + tablero.tablero_1()["d2"] + " " + tablero.tablero_1()["d3"] + " " + tablero.tablero_1()["d4"] + " " + tablero.tablero_1()["d5"]
    e = tablero.tablero_1()["e1"] + " " + tablero.tablero_1()["e2"] + " " + tablero.tablero_1()["e3"] + " " + tablero.tablero_1()["e4"] + " " + tablero.tablero_1()["e5"]
    abcde = a, b, c, d, e
    print("   A B C D E")
    for n,x in enumerate(abcde):
        print(n+1,"|" + x)
diccionario_a_formato_agradable()
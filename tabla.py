def diccionario_a_formato_agradable():
    tablero_1 = {"a1": "o","a2": "o","a3": ".","a4": "o","a5": "o",
                 "b1": "o","b2": ".","b3": "o","b4": ".","b5": "o",
                 "c1": ".","c2": "o","c3": "o","c4": "o","c5": ".",
                 "d1": "o","d2": ".","d3": "o","d4": ".","d5": "o",
                 "e1": "o","e2": "o","e3": ".","e4": "o","e5": "o"}
    a = tablero_1["a1"] + " " + tablero_1["a2"] + " " + tablero_1["a3"] + " " + tablero_1["a4"] + " " + tablero_1["a5"]
    b = tablero_1["b1"] + " " + tablero_1["b2"] + " " + tablero_1["b3"] + " " + tablero_1["b4"] + " " + tablero_1["b5"]
    c = tablero_1["c1"] + " " + tablero_1["c2"] + " " + tablero_1["c3"] + " " + tablero_1["c4"] + " " + tablero_1["c5"]
    d = tablero_1["d1"] + " " + tablero_1["d2"] + " " + tablero_1["d3"] + " " + tablero_1["d4"] + " " + tablero_1["d5"]
    e = tablero_1["e1"] + " " + tablero_1["e2"] + " " + tablero_1["e3"] + " " + tablero_1["e4"] + " " + tablero_1["e5"]
    abcde = a, b, c, d, e
    print("   A B C D E")
    for n,x in enumerate(abcde):
        print(n+1,"|" + x)
diccionario_a_formato_agradable()
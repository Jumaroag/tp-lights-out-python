def lista_a_formato_agradable():
    tablero_1 = [["o", "o", ".", "o", "o"],
                 ["o", ".", "o", ".", "o"],
                 [".", "o", "o", "o", "."],
                 ["o", ".", "o", ".", "o"],
                 ["o", "o", ".", "o", "o"]]
    a = tablero_1[0][0] + " " + tablero_1[0][1] + " " + tablero_1[0][2] + " " + tablero_1[0][3] + " " + tablero_1[0][4]
    b = tablero_1[1][0] + " " + tablero_1[1][1] + " " + tablero_1[1][2] + " " + tablero_1[1][3] + " " + tablero_1[1][4]
    c = tablero_1[2][0] + " " + tablero_1[2][1] + " " + tablero_1[2][2] + " " + tablero_1[2][3] + " " + tablero_1[2][4]
    d = tablero_1[3][0] + " " + tablero_1[3][1] + " " + tablero_1[3][2] + " " + tablero_1[3][3] + " " + tablero_1[3][4]
    e = tablero_1[4][0] + " " + tablero_1[4][1] + " " + tablero_1[4][2] + " " + tablero_1[4][3] + " " + tablero_1[4][4]
    abcde = a, b, c, d, e
    print("   A B C D E")
    for n,x in enumerate(abcde):
        print(n+1,"|" + x)
lista_a_formato_agradable()

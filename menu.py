def saludo_de_bienvenida():
    hola = " ¡¡ Hola !! "
    print(hola.center(50, "="))
    bienvenido = " ¡ Bienvenido a Lights Out ! "
    print(bienvenido.center(50, "="))
    print()

def eleccion_nivel():
    print("¿Que modo deseas jugar?")
    print("1-Jugar Niveles")
    print("2-Jugar Random")
    print("3-Salir")
    a = input()
    a = str(a)
    if (a == "1"):
        print("Usted eligio hacer los niveles predetermiandos...")
    elif (a == "2"):
        print("Usted eligio hacer un nivel aleatorio...")
    elif (a == "3"):
        print("SALIR")
    else:
        print("Opción no válida, elija 1, 2 o 3")
        eleccion_nivel()
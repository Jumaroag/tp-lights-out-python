print("¡Hola!")
print("¡Bienvenido a Lights Out!")
def eleccion_nivel():
    print("¿Que modo deseas jugar?")
    print("1-Jugar Niveles")
    print("2-Jugar Random")
    print("3-Salir")
    a = input()
    if (int(a) == 1):
        print("Usted eligio hacer los niveles predetermiandos...")
    elif (int(a) == 2):
        print("Usted eligio hacer un nivel aleatorio...")
    elif (int(a) == 3):
        print("SALIR")
    else:
        eleccion_nivel()
eleccion_nivel()
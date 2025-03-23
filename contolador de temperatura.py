
def sensor(temperatura):
    if temperatura <10:
        print(" se acaba de activar un calefactor")
    elif temperatura >=10 and temperatura <25:
        print(" no se activa nada ")
    elif temperatura >=25:
        print(" se va activar el ventilador ")
def tomar_datos():
    return int(input(" ingrese un numero: "))

while True:
    print(" menu ")
    print(" bienvenido ")
    print(" 1. ingrese la temperatura ambiente ")
    print(" 2. finalizar ")
    opcion=int(input(" ingrese la seleccion "))
    if opcion==1:
        temperatura=tomar_datos()
        sensor(temperatura)
    
    elif opcion==2:
            print(" nos vemos pronto ")
            break
    else:
            print(" numero no especificado  ")
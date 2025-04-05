def menu1():
    print("\nMenu:")
    print("-Pulsa 1 para iniciar el control de luces:")
    print("-Pulsa 2 para salir del sistema:")
    return int(input("\nDigite su opción: "))
def menu():
    return input("\n¿Desea Continuar en el sistema?:(si/no) ").upper()
def datos():
    import random
    noche=random.choice([True,False])
    mov=random.choice([True,False])
    return noche,mov
def ControlLuces(noche,mov):
    if noche==True and mov==True:
        print(f"\n¿Es de noche?: {noche}, ¿Hay movimiento en la habitación?: {mov}")
        print("!LUCES ENCENDIDAS¡")
    else:
        print(f"\n¿Es de noche?: {noche}, ¿Hay movimiento en la habitación?: {mov}")
        print("!LUCES APAGADAS¡")
def mostrar():
    opc1=menu1()
    while opc1==1:
        import time
        noche,mov=datos()
        ControlLuces(noche,mov)
        opc=menu()
        if opc=="si":
            time.sleep(10)
        else:
            print("\nSu ejecución ha finalizados...\n")
            break
#****Codigo Primcipal****
print("\n----------CONTROL DE LUCES----------")
mostrar()
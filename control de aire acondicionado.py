def menu1():
    print("\nMenu:")
    print("-Pulsa 1 para iniciar el control de Aire Acondicionado:")
    print("-Pulsa 2 para salir del sistema:")
    return int(input("\nDigite su opción: "))
def menu():
    return input("\n¿Desea Continuar en el sistema?:(si/no) ").upper()
def tomar_dato():
    Temperatura=float(input("\n¿Cual es la temperuta actual de su ambiente?:"))
    humedad=float(input("¿Cual es el porcentaje de la humedad?:"))
    return Temperatura,humedad
def ControlAire(Temperatura,humedad):
    if Temperatura>28 and humedad>60 or Temperatura>30:
        print("\n!AIRE ACONDICIONADO ENCENDIDO¡")
    else:
        print("\nAIRE ACONDICIONADO APAGADO")
def mostrar():
    opc1=menu1()
    while opc1==1:
        import time
        Temperatura,humedad=tomar_dato()
        ControlAire(Temperatura,humedad)
        opc=menu()
        if opc=="SI":
            time.sleep(3)
        else:
            print("\nSu ejecución ha finalizados...\n")
            break
#****Codigo Primcipal****
print("\n----------CONTROL DE AIRE ACONDICIONADO----------")
mostrar()
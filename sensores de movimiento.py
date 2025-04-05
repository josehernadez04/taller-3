def menu():
    print("\nMENU")
    print("1. Pulsa 'A' para ACTIVAR la alarma Automaticamente")
    print("2. Pulsa 'D' para DESACTIVAR la alarma Automaticamente")
    print("3. Pulse 'C' para finalizar y salir del sitema")
    return input("\nDigite su opción: ").upper()
def Alarma(opc):
    if opc=="A":
        print("\nLa alarma ha sido ACTIVADA")
    elif opc=="D":
        print("\nLa alarma ha sido DESACTIVADA")
    else:
        print("\nOpción invalida, de acuerdo al MENÚ intente nuevamente:")
        opc=menu()
def Detector():
    import time
    import random
    noche=random.choice([True,False])
    sensor1=random.choice([True,False])
    sensor2=random.choice([True,False])
    sensor3=random.choice([True,False])
    if noche==(True and sensor1==True and sensor2==True) or\
      (noche==True and sensor1==True and sensor3==True) or\
      (noche==True and sensor2==True and sensor3==True):
        print(f"\n¿Es de noche?: {'Si'if noche else 'No'}, ¿Hay movimiento detectado?: Sensor 1: {'Si'if sensor1 else 'No'},Sensor 2: {'Si'if sensor2 else 'No'}, Sensor 3;{'Si'if sensor3 else 'No'}")
        print("¡ALARMA ACTIVADA!\n")
    else:
        print(f"\n¿Es de noche?: {'Si'if noche else 'No'}, ¿Hay movimiento detectado?: Sensor 1: {'Si'if sensor1 else 'No'}, Sensor 2: {'Si'if sensor2 else 'No'}, Sensor 3;{'Si'if sensor3 else 'No'}")
        print("¡ALARMA DESACTIVADA!\n")
    time.sleep(3)

def mostrar():
    while True:
        opc=menu()
        if opc=="C":
            print("\nSu ejecución ha finalizado\n")
            break
        else:
            Alarma(opc)
            Detector()

#*********Codigo principal**********
print("*************** DETECTOR DE INTRUSOS ******************")
print("BIENVENIDO AL SISTEMA DE SEGURIDAD DE DETECCIÓN DE INTRUSOS DE MANERA AUTOMÁTICA")
mostrar()
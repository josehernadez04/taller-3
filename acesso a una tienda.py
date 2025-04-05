def tomar_datos():
    nombre=input(f"\n¿Cual es tu nombre?: ").capitalize()
    membresia=input(f"¿Tiene membresía?(si/no): ").lower()
    empleado=input(f"¿Eres empleado?(si/no): ").lower()
    return nombre,membresia,empleado

def dentro_horario():
    from datetime import datetime
    horario_atención=(7, 20)
    hora_actual=datetime.now().hour
    return horario_atención[0] <= hora_actual < horario_atención[1]

def validarEntrada(nombre,menbresia,empleado,horario):
    if menbresia=="SI" and horario==True or empleado=="SI":
        print(f"ACCESO PERMITIDO. ¡Bienvenid@ {nombre}!")
    else:
        print(f"ACCESO DENEGADO. Lo sentimos {nombre}.")
def mostrar():
    import time
    while True:
        nombre,menbresia,empleado=tomar_datos()
        horario=dentro_horario
        validarEntrada(nombre,menbresia,empleado,horario)
        time.sleep(3)


#*******Código Principal*******
mostrar()
def tomar_nun1():
    num1 = float(input(" ingrese el primer numero: "))
    return num1
def tomar_nun2():
    num2 = float(input(" ingrese el segundo numero: "))
    return num2
def suma():
    aux1=tomar_nun1()
    aux2=tomar_nun2()
    reult= aux1 + aux2
    return reult
def resta():
    se=tomar_nun1()
    so=tomar_nun2()
    reult=se-so
    return reult
def mult():
    ce=tomar_nun1()
    ca=tomar_nun2()
    reult= ce*ca
    return reult
def div():
    eco=tomar_nun1()
    sol=tomar_nun2()
    reult=eco/sol
    return reult
while True:
    print(" elegi el operador '+'. suma")
    print(" elegi el operador '-'.resta ")
    print(" elegi el operador '*'.multiplicar ")
    print(" elegi el operador '/'. divicion ")
    operador=input(" ingrese el operador ")
    if operador=="+":
        print(" la suma es:",suma())
    elif operador=="-":
        print(" la resta es:",resta())
    elif operador=="*":
        print(" la multiplicacion es:",mult())
    elif operador=="/":
          print(" la division es: ",div())
    else:
        print(" operador incorrecto ")
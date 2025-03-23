import os
def tomar_datos():
        return int(input(" ingrese un numero: "))
def jugar(num):
         if num % 3 ==0 and num % 5 == 0:
                print(" FizzBuzz")
         elif num % 3 ==0:
                print(" Fizz ")
         elif num % 5 ==0:
                print(" Buzz ")
         else:
                 print(f"el numero {num} no es visible por entre 3 y 5 ")
def menu():
        print(" este programa es un juego ")
        print(" si el numero es divisible por 3, imprime 'Fizz' ")
        print(" si el numero es divisible por 5 va a salir Buzz")
        print(" y si el numero es divisible por 3 y por 5 va a salir FizzBuzz ")
        print(" 1. si deseas jugar ")
        print(" 2. si deseas salir ")
        opc=int(input(" digite tu opcion: "))
        return opc
opc=0
while opc!=2:
    os.system("cls")
    opc=menu()
    if opc==1:
            num=tomar_datos()
            jugar(num)
    elif opc==2:
            print(" gracias por jugar ")
    else:
            print(" la opcion esta erranea ")
    input(" dele enter para continuar ")
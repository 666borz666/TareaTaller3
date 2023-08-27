#Elaborado por Daniel Campos
#Creacion 26-08-2023 3:00 pm
#Ultima mod 26-08-2023 
#Version 3.10.6

from funciones import *
#1
def sacarParesAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n, str)==True:
        print("Debe ingresar únicamente números.")
    elif n==0:
        print("Debe ingresar números diferentes de 0.")
    else:
        return sacarPares(n)

def opcionSacarPares(n):
    """
    F: Entrada y salida de datos de la funcion sacar pares
    E: Número n
    S: Dígitos del número n que son pares
    """
    print("Dígitos pares de un número.")
    n=int(input("Digite un número diferente de 0: "))
    print(sacarPares(n))
 #2   
def opcionCalcularMasgrande(n):
    """
    F: Entrada y salida de datos de la función calcular más grande
    E: Número n
    S: Cifra del número n más grande
    """
    print("Dígitos más grande de un número.")
    n=int(input('Digite un numero entero positivo:'))
    print(calcularMasgrande(n))
    
def calcularMasgrandeAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    return 
#3
def opcionMultiplicarImpares(n):
    """
    F: Entrada y salida de datos de la función multiplicar impares
    E: Numero n
    S: Resultado de la múltiplicacion de los dígitos impares del número n
    """
    print("Multiplicar dígitos impares de un número.")
    n=int(input('Digite un numero entero positivo:'))
    print(multiplicarImpares(n))
    
def multiplicarImparesAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    return
#4
def opcionSacarValorPosicionesImpares(n):
    """
    F: Entrada y salida de datos de la función multiplicar impares
    E: Número n
    S: Dígitos en las posiciones impares
    """
    print("Dígitos en las posiciones impares de un número")
    n=int(input('Digite un numero entero positivo:'))
    print(sacarValorPosicionesImpares(n))
    
def sacarValorPosicionesImparesAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    return

#menu
def menu():
    """
    Funcionamiento: De manera repetitiva, muestra el menú al usuario. 
    Entradas: NA
    Salidas: Resultado según lo solicitado
    """
    n=0
    print ("1. Dígitos pares")
    print ("2. Dígito más grande")
    print ("3. Multiplicar dígitos impares")
    print ("4. Dígitos en posiciones impares")
    print ("0. Terminar")
    opcion = int (input ("Escoja una opción: "))
    if opcion >=0 and opcion <=4:
        if opcion == 1:
            opcionSacarPares(n)
        elif opcion == 2 :
            opcionCalcularMasgrande(n)
        elif opcion == 3:
            opcionMultiplicarImpares(n)
        elif opcion == 4:
            opcionSacarValorPosicionesImpares(n)
        else:
            return
    else:
        print ("Opción inválida")
        
#programa principal
menu()
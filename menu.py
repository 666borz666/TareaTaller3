#Elaborado por Daniel Campos
#Creacion 26-08-2023 3:00 pm
#Ultima mod 27-08-2023 9:17 am
#Version 3.10.6

from funciones import *
#1
def sacarParesAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        sacarPares(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""
    
def opcionSacarPares(n):
    """
    F: Entrada y salida de datos de la funcion sacar pares
    E: Número n
    S: Dígitos del número n que son pares
    """
    while True:
        try:
            print("Dígitos pares de un número.")
            n=int(input('Digite un numero entero positivo:'))
            return  print(sacarParesAux(n))
        except:
            return print("Debe ingresar un número, no ingrese caracteres diferentes de números.")   
 #2   
def calcularMasgrandeAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        calcularMasgrande(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""
    
def opcionCalcularMasgrande(n):
    """
    F: Entrada y salida de datos de la función calcular más grande
    E: Número n
    S: Cifra del número n más grande
    """
    while True:
        try:
            print("Dígitos más grande de un número.")
            n=int(input('Digite un numero entero positivo: '))
            return print(calcularMasgrandeAux(n))
        except:
            return print("Debe ingresar un número, no ingrese caracteres diferentes de números.")   
#3
def multiplicarImparesAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        multiplicarImpares(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""
    
def opcionMultiplicarImpares(n):
    """
    F: Entrada y salida de datos de la función multiplicar impares
    E: Numero n
    S: Resultado de la múltiplicacion de los dígitos impares del número n
    """
    while True:
        try:
            print("Multiplicar dígitos impares de un número.")
            n=int(input('Digite un numero entero positivo: '))
            return print(multiplicarImparesAux(n))
        except:
            return print("Debe ingresar un número, no ingrese caracteres diferentes de números.")    
    
#4
def sacarValorPosicionesImparesAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Número n
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        sacarValorPosicionesImpares(n)
        if n<=0:
            return "El número debe ser diferente de cero."
    else: 
        return "Debe ingresar sólo números."
    return ""
    
def opcionSacarValorPosicionesImpares(n):
    """
    F: Entrada y salida de datos de la función multiplicar impares
    E: Número n
    S: Dígitos en las posiciones impares
    """
    print("Dígitos en las posiciones impares de un número")
    while True:
        try:
            print("Mostrar los dígitos en las posiciones impares.")
            n=int(input('Digite un numero entero positivo: '))
            return print(sacarValorPosicionesImparesAux(n))
        except:
            return print("Debe ingresar un número, no ingrese caracteres diferentes de números.")
    return ""
    
    
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
    while True:
        try:
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
                return print ("Opción inválida")
        except:
            return print("Debe ingresar un número, no ingrese caracteres diferentes de números.")
    
def menuAux(n):
    """
    F: Revisa que los datos de entrada sean los correctos
    E: Opción del menú seleccionada
    S: Función seleccionada
    """
    if isinstance(n,int)==True:
        menu(n)
    else: 
        return "Debe ingresar sólo números."
    return ""
        
#programa principal
menu()
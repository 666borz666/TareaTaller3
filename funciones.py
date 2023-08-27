#Elaborado por Daniel Campos
#Creacion 26-08-2023 3:00 pm
#Ultima mod 27-08-2023 9:17am
#Version 3.10.6

#definicion de funciones
#digitos pares
#1
def sacarPares(n):
    """
    F: Del número n, separa los dígitos que son pares y los muestra
    E: Número n
    S: Dígitos del número n que son pares
    """
    while n>0:
        x=int(n%10)
        if x%2==0:
            print("Dígito par: ",x)
        else:
            print("Dígito impar.")
        n=n//10
    return ""

#numero mas grande de la cifra
#2
def calcularMasgrande(n):
    """
    F: Del número n, calcula la cifra con mayor tamaño
    E: Número n
    S: Cifra del número n más grande
    """
    mayor=0
    menor=0
    while n>0:
        x=int(n%10)
        if x>mayor:
            mayor=x
        else:
            menor=x
        n=n//10
    return print(mayor)

#multiplicar numeros impares
#3
def multiplicarImpares(n):
    """
    F: Del número n, separa los dígitos que son impares y los multiplica
    E: Numero n
    S: Resultado de la múltiplicacion de los dígitos impares del número n
    """
    multi=1
    par=0
    while n>0:
        x=int(n%10)
        if x%2!=0:
            print("Dígito impar: ",x)
            multi=multi*x
            print("Multiplicación: ",multi)
        if x%2==0:
            par=0*x
            print("0")
        n=n//10
    return ""
#valores de las posiciones impares
#4
def sacarValorPosicionesImpares(n):
    """
    F: Del número n, lee la cantidad de cifras que tiene y, de las cifras que son impares, muestra el número en esa posición
    E: Número n
    S: Dígitos en las posiciones impares
    """
    i=0
    while n>0:
        x=int(n%10)
        if i%2!=0:
            print(x)
        else:
            print("\n","")
        i+=1
        n=n//10
    return ""
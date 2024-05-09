# Ejercicio 8

from math import sqrt, pow


def ingresar_num():
    while True:
        try:
            num = int(input("Ingrese un numero: "))
            return num
        except ValueError:
            print("Error: No es un número entero")


def raiz_num(num):
    raiz = round(sqrt(num), 2)
    print(f"El valor de la raiz es: {raiz}")


def potencia_num(num):
    cuadrado = pow(num, 2)
    cubo = pow(num, 3)
    print(f"El cuadrado es: {cuadrado}"
          f" y el cubo es: {cubo}")


# Función principal:
def main():
    num = ingresar_num()
    raiz_num(num)
    potencia_num(num)


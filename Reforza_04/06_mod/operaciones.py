# Ejercicio 6

def ingresar_int():
    while True:
        try:
            num = int(input("Ingrese un número entero: "))
            return num
        except ValueError:
            print("Error: El Número debe ser entero")
        except:
            print("Error: Ingrese un valor válido")


def sumar_valores():
    num1 = ingresar_int()
    num2 = ingresar_int()
    return num1 + num2



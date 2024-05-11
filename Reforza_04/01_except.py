
def funcion_1():
    try:
        suma = 80 + "Hola Pythonista"
        return suma
    except TypeError:
        print("Error: No se puede ejecutar una suma con dato tipo 'str'")
    else:
        print("Error: No se puede realizar la suma")


funcion_1()

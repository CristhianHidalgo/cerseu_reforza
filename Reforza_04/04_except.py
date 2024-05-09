
string = "Hello Pythonista"

def funcion_4(string):
    try:
        print(string/0)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre 0")
    except TypeError:
        print("Error: No se puede operar con un dato tipo string")
    else:
        print("Error: Operación no ejecutable")

funcion_4(string)
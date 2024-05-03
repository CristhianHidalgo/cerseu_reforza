
var_1 = input("Ingrese una oración con más de 2 palabras: ")

def contar_palabras(var_1):
    lista_palabras = var_1.split()
    cantidad = len(lista_palabras)

    if cantidad >= 3:
        return print(f"La cantidad de palabras es: {cantidad}")
    else:
        return print("Ha ingresado una oración con menos de 3 palabras")

contar_palabras(var_1)
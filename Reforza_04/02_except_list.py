
lista = [2, 6, 10, 4, 5, 23, 1]

def funcion_2(lista):
    try:
        lista[10]
    except IndexError:
        print("Error: El índice buscado supera el rango de datos")

funcion_2(lista)
# Ejercicio 7

import random


def lista_aleatoria():
    lista = []
    for i in range(0, 30):
        lista.append(random.randint(1, 100))
    return lista


def ordenar_lista():
    lista = lista_aleatoria()
    print(lista)
    lista.sort()
    return lista

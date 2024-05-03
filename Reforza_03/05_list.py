
cantidad = int(input("Ingrese la cantidad de valores a añadir a la lista: "))
lista = []
def eliminar_valor(lista, eliminar):
    contador = 0
    while cantidad > contador:
        numero = int(input("Ingrese un número a añadir a la lista: "))
        lista.append(numero)
        contador += 1

    eliminar = int(input("Ingrese el número a eliminar de la lista: "))
    print(f"La lista original es: {lista}")

    if eliminar in lista:
        lista.remove(eliminar)
        print(f"La lista actualizada es: {lista}")
    else:
        print("El valor no se encuentra en la lista")
        print(f"La lista actualizada es: {lista}")
    print(f"El número a eliminar fue: {eliminar}")

eliminar_valor(lista, cantidad)



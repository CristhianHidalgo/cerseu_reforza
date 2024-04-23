
# 18. Lista con 15 primeros números impares

lista = []
impar = 1

lista.append(impar)

while impar < (15 - 1) * 2:
    impar = impar + 2
    lista.append(impar)

# Añadiendo 3 número flotantes repetidos

lista.append(17.0)
lista.append(17.0)
lista.append(17.0)

# Agregando una cadena en la posición 3 de la lista

lista.insert(3, "Python")

# Eliminamos un valor impar de la cadena

del lista [8]

print(f"La lista actualizada es: {lista}")


num_1 = int(input("Ingrese un numero: "))
num_2 = int(input("Ingrese un numero: "))

cuadrados_1 = []
cuadrados_2 = []

def cuadrado(num_1, num_2):
    if num_1 > num_2:
        contador = num_2 + 1
        while contador < num_1:
            cuadrados_1.append(pow(contador, 2))
            contador += 1
        return print(f"Los cuadrados de los número entre {num_2} y {num_1} son: {cuadrados_1}")

    elif num_2 > num_1:
        contador = num_1 + 1
        while contador < num_2:
            cuadrados_2.append(pow(contador, 2))
            contador += 1
        return print(f"Los cuadrados de los número entre {num_1} y {num_2} son: {cuadrados_2}")

    else:
        print("Los números son iguales")

cuadrado(num_1, num_2)
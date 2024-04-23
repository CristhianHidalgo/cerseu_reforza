# 19. Ingresar 10 valores y calcular suma y media

lista = []
contador = 0

while contador < 10:
    lista.append(int(input("Ingresa un número entero: ")))
    contador += 1

suma = sum(lista)
print(f"\nLa suma de los valores ingresados es: {suma}")

media = suma / len(lista)
print(f"\nLa media de los valores ingresados es: {media: .1f}")
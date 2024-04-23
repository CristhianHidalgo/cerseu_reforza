
# 17. Lista con 10 primeros números al cuadrado

lista = []
contador = 1    # Comenzamos desde la unidad 1
num_cuadrado = 0  # Puede ir cualquier número

while contador <= 10:
    num_cuadrado = pow(contador, 2)
    lista.append(num_cuadrado)
    contador = contador + 1

print(f"Los 10 primeros números al cuadrado son: {lista}")
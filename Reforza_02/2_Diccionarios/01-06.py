# 1. Creación de diccionario

empleado = {"nombre": "Alberto", "edad": 35, "salario": 4500}

# 2. Convertir diccionario a lista

lista = list(empleado)
print(f"\nEl tipo de dato actualizado es: {type(lista)}")

# 3. Agregar un nuevo key 'DNI'

empleado["DNI"] = "03758245"
print(f"El valor de salrio es: {empleado["salario"]}")

# 4. Eliminar el key 'Edad'

del empleado["edad"]

# 5. Convertir diccionario a lista

lista_1 = list(empleado)
print(f"El tipo de dato actualizado es: {type(lista_1)}")

# 6. Crear un diccionario con los mismos valores

usuario = empleado

print (f"El nuevo diccionario es: {usuario}")
# 11. Mostrar valores por índice

lista = [True, 14.78, 18.54, False, 24.58, False, 17.58]
print(f"El penúltimo valor de la lisa es {lista[-2]} y el último es {lista[-1]}")

# 12. Reconocer tipo de datos

print(f"\nEl tipo de dato del primer valor '{lista[0]}' es {type(lista[0])}"
      f"\nEl tipo de dato del segundo valor '{lista[1]}' es {type(lista[1])}"
      f"\nEl tipo de dato del tercer valor '{lista[2]}' es {type(lista[2])}"
      f"\nEl tipo de dato del cuarto valor '{lista[3]}' es {type(lista[3])}"
      f"\nEl tipo de dato del quinto valor '{lista[4]}' es {type(lista[4])}"
      f"\nEl tipo de dato del sexto valor '{lista[5]}' es {type(lista[5])}"
      f"\nEl tipo de dato del septimo valor '{lista[6]}' es {type(lista[6])}")

# 13. Eliminar todos los datos de la lista

lista.clear()
print(f"\nLa lista actualizada es la siguiente: {lista}")

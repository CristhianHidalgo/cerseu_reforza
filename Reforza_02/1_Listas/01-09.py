# 1. Crear una lita
cursos = ["Calculo", "Física", "Química", "Ingles", "Geología Estructural", "Mecánica de Fluidos"]

# 2. Agregar objetos

cursos.append("Geomecánica")
cursos.append("Geoestadística")
cursos.append("Geología de Yacimientos")
cursos.append("Legislación")
cursos.append("Comercialización de Minerales")
cursos.append("Mecánica de Rocas")

# 3. Eliminar objetos

cursos.remove("Ingles")
cursos.remove("Legislación")

# 4. Invertir lista

cursos.reverse()
print(f"La lista hasta el paso 4. es {cursos}")

# 5. Cantidad de objetos

cantidad_cursos = len(cursos)
print(f"La cantidad de cursos en la lista es {cantidad_cursos}")

# 6. Repetición de objetos

cursos.append("Geomecánica")
cursos.append("Geomecánica")
cantidad_geomecanica = cursos.count("Geomecánica")
print(f"La cantidad de veces que se repite 'Geomecánica' es: {cantidad_geomecanica}")

# 7. Borrar primer objeto

cursos.pop(0)
print(f"La lista actualizada es {cursos}")

# 8. Nueva lista

lista = []
lista.append(20.78)
lista.append("Python")
lista.append(14.59)
lista.append(85)
lista.append("Java")
lista.append(500)
lista.append("Ruby")
lista.append(65.87)
lista.append(333)

# 9. Suma de listas

suma = cursos + lista
print(f"Las suma lista es {suma}")

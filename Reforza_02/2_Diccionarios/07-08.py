
# 7. Diccionario con 6 departamentos del país

depart = {1: "Piura", 2: "Lima", 3: "Arequipa", 4: "Cusco", 5: "Cajamarca", 6: "Moquegua"}
del depart[5]
print (f"\nEl diccionario actualizado es: {depart}")

# 8. Agregar un elemento al diccionario

depart["carrera"] = "Ingeniería de Minas"
depart_valores = list(depart.values())
print(f"Los valores de la variable final son: {depart_valores}")


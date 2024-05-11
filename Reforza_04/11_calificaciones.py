
def ingresar_datos():
    nombre = input("Ingrese el nombre del alumno: ")
    nota_1 = float(input("Ingrese la nota 1: "))
    nota_2 = float(input("Ingrese la nota 2: "))
    promedio = (nota_1 + nota_2) / 2
    return nombre, promedio


def leer_fichero():
    nombre, promedio = ingresar_datos()
    file = open("ficheros/calificaciones.txt", "a+")

    if promedio > 10:
        file.write(f"{nombre}, aprobado")
    else:
        file.write(f"{nombre}, desaprobado")

    file = open("ficheros/calificaciones.txt", "r")
    print(file.read())
    file.close()


leer_fichero()


def nombre_apellido(nombre, apellido):
    return nombre + " " + apellido


def tipo_seguro(seguro):
    return seguro


def mayor_edad():
    while True:
        try:
            edad = int(input("Ingrese la edad: "))
            break
        except ValueError:
            print("Ingrese un valor entero")

    if edad >= 18:
        return "es mayor de edad"
    else:
        return "no es mayor de edad"

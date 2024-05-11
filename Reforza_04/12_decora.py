
def funcion_decoradora(funcion_parametro):
    def funcion_interna(*args):
        print("Buenos días!")
        funcion_parametro(*args)
        print("Hasta luego")
    return funcion_interna


@funcion_decoradora
def presentacion(nombre):
    print(f"Soy {nombre}")


nombre = input("Ingrese el nombre de la persona que desea presentar: ")
presentacion(nombre)


def funcionD(funcionP):
    def funcionI(*args):
        print("La cantidad de argumentos que tiene la función es")
        funcionP(*args)
        print("La función decoradora termin+o de ejecutarse correctamente")
    return funcionI


@funcionD
def suma(a, b, c, d):
    parametros = locals()
    cantidad = len(parametros)
    print(cantidad)


suma(2, 3, 5, 4)

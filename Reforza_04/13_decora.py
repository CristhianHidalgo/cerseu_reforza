
def funcionA(funcionB):
    def funcionC(*args):
        print("Está por ejecutarse la función")
        funcionB(*args)
        print("La función ha sido ejecutada correctamente")
    return funcionC

@funcionA
def multiplicacion(num_1, num_2, num_3, num_4):
    mult = num_1 * num_2 * num_3 * num_4
    print(mult)

num_1 = int(input("Ingrese el primer numero: "))
num_2 = int(input("Ingrese el segundo numero: "))
num_3 = int(input("Ingrese el tercer numero: "))
num_4 = int(input("Ingrese el cuarto numero: "))

multiplicacion(num_1, num_2, num_3, num_4)


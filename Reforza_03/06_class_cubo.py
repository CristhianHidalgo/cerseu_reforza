
class Numero:
    def __init__(self):
        self.num = 0
        self.cubo = 0
        self.cuadrado_cubo = 0

    def ingresar_numero(self):
        self.num = int(input("Ingrese un numero: "))

    def operacion_cubo(self):
        self.cubo = pow(self.num, 3)

    def cuadrado_resultado(self):
        self.cuadrado_cubo = pow(self.cubo, 2)

num_1 = Numero()
num_1.ingresar_numero()
num_1.operacion_cubo()
num_1.cuadrado_resultado()

print(f"El número ingresado fue: {num_1.num}")
print(f"El cubo del número ingresado es: {num_1.cubo}")
print(f"El cuadrado del cubo del número ingresado es: {num_1.cuadrado_cubo}")

class Usuario:
    def __init__(self):
        self.nombre_apellido = False
        self.edad = 0

    def ingresar_datos(self):
        self.nombre_apellido = input("Ingrese su nombre y apellido: ")
        self.edad = int(input("Ingrese su edad: "))

    def imprimir_resultado(self):
        self.diccionario = {"nombre y apellido": self.nombre_apellido, "edad": self.edad}

usuario_1 = Usuario()
usuario_1.ingresar_datos()
usuario_1.imprimir_resultado()
print(usuario_1.diccionario)

class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.bonificacion = 0

    def mayor_edad(self):
        if self.edad >= 18:
            print("La persona es mayor de edad")
        else:
            print("La persona es menor de edad")

    def bonificar(self):
        self.bonificacion = self.sueldo * 1.2
        print(f"El sueldo con bonificación incluida es {self.bonificacion}")

persona_1 = Persona("Carlos", 26, 5000)
persona_1.mayor_edad()
persona_1.bonificar()

persona_2 = Persona("Lucia", 17, 1500)
persona_2.mayor_edad()
persona_2.bonificar()





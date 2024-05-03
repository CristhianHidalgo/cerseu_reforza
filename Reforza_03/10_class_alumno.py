
class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def imprimir(self):
        print(f"\nEl alumno {self.nombre}, tiene {self.edad} años y {self.nota_final} de nota final")

    def aprobado_nota(self):
        if self.nota_final >= 11:
            print(f"El alumno esta aprobado con {self.nota_final} de nota final")
        else:
            print(f"El alumno esta desaprobado con {self.nota_final} de nota final")

alumno_1 = Alumno("Carlos", 21, 19)
alumno_1.imprimir()
alumno_1.aprobado_nota()

alumno_2 = Alumno("Juanita", 23, 10)
alumno_2.imprimir()
alumno_2.aprobado_nota()

alumno_3 = Alumno("Juan", 19, 15)
alumno_3.imprimir()
alumno_3.aprobado_nota()


class Persona:
    def __init__(self):
        self.nombre = input("\nIngrese el nombre de la persona: ")
        self.edad = int(input("Ingrese el edad de la persona: "))

class Empleado(Persona):
    def __init__(self, sueldo):
        super().__init__()
        self.sueldo = sueldo

    def pagar_impuesto(self):
        if self.sueldo > 4000:
            self.impuesto = self.sueldo * 0.1
            print("El impuesto a pagar es: ", self.impuesto)
        else:
            print("El impuesto a pagar es: 0")

empleado_1 = Empleado(5000)
print(f"El saldo del empleado es: {empleado_1.sueldo}")
empleado_1.pagar_impuesto()

empleado_1 = Empleado(3000)
print(f"El saldo del empleado es: {empleado_1.sueldo}")
empleado_1.pagar_impuesto()
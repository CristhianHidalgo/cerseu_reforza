import math

class Circulo:
    def __init__(self):
        self.radio = 0
        self.area = 0
        self.perimetro = 0

    def radio_solicitar(self):
        while True:
            try:
                self.radio = float(input("Ingrese el radio del circulo: "))
                break
            except ValueError:
                print("Opps! El valor ingresado no es un número")

    def area_circulo(self):
        self.area = math.pi * pow(self.radio, 2)

    def perimetro_circulo(self):
        self.perimetro = 2 * math.pi * self.radio

circulo_1 = Circulo()
circulo_1.radio_solicitar()
circulo_1.area_circulo()
circulo_1.perimetro_circulo()

print(f"El radio del circulo 1 es: {circulo_1.radio: .2f}")
print(f"El perimetro del circulo 1 es: {circulo_1.perimetro: .2f}")
print(f"El area del circulo 1 es: {circulo_1.area: .2f}\n")


circulo_2 = Circulo()
circulo_2.radio_solicitar()
circulo_2.area_circulo()
circulo_2.perimetro_circulo()

print(f"El radio del circulo 2 es: {circulo_2.radio: .2f}")
print(f"El perimetro del circulo 2 es: {circulo_2.perimetro: .2f}")
print(f"El area del circulo 2 es: {circulo_2.area: .2f}")
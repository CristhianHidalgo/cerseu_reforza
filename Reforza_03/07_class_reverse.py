
class Palabra:
    def __init__(self):
        self.palabra = "Hola Pythonistas, seguimos adelante"
        self.invertida = 0

    def invertir(self):
        self.lista = self.palabra.split()
        self.lista.reverse()
        self.invertida = " ".join(self.lista)

oracion_1 = Palabra()
oracion_1.invertir()
print(f"La cadena de palabras invertida es: {oracion_1.invertida}")

oracion_2 = Palabra()
oracion_2.invertir()
print(f"La cadena de palabras invertida es: {oracion_2.invertida}")


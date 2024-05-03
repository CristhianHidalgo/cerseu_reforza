
class Contacto:
    def __init__(self):
        self.nombre = False
        self.telefono = 0
        self.email = False
        self.DNI = False
        self.dicc = {}
        self.lista = []

    def añadir_contacto(self):
        self.nombre = input("\nIngrese el nombre del contacto: ")
        self.telefono = int(input("Ingrese el telefono del contacto: "))
        self.email = input("Ingrese el email del contacto: ")
        self.DNI = input("Ingrese el DNI del contacto: ")

        self.dicc = {"nombre": self.nombre, "telefono": self.telefono, "email": self.email, "DNI": self.DNI}
        self.lista.append(self.dicc)

    def mostrar_contactos(self):
        contacto = print(f"La lista de contactos es: {self.lista}\n")
        return contacto

    def buscar_contacto(self):
        self.DNI_buscado = input("Ingrese el DNI del contacto: ")

        for self.dicc in self.lista:
            if  self.DNI_buscado in self.dicc.values():
                self.valor = self.dicc["nombre"]
                print(f"El contacto buscado es: {self.valor}")
            else:
                print(f"El valor {self.DNI_buscado} no se encuentra en agenda")

agenda_1 = Contacto()
agenda_1.añadir_contacto()
agenda_1.mostrar_contactos()
agenda_1.buscar_contacto()






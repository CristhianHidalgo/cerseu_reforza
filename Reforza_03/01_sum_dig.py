
var_1 = int(input("Ingrese el primer número: "))
var_2 = int(input("Ingrese el segundo número: "))

lista_digito1 = []
lista_digito2 = []

for digito in str(var_1):
    lista_digito1.append(int(digito))

for digito in str(var_2):
    lista_digito2.append(int(digito))

suma_1 = sum(lista_digito1)
suma_2 = sum(lista_digito2)

def suma_digitos(var_1, var_2):
   if suma_1 > suma_2:
       print(f"La suma de dígitos de {var_1} es mayor")
   else:
       print(f"La suma de dígitos de {var_2} es mayor")

   if suma_1 > 10:
       print(f"La suma de dígitos de {var_1} es mayor de 10")
   if suma_2 > 10:
       print(f"La suma de dígitos de {var_2} es mayor de 10")
   else:
       print(f"Ninguna suma de dígitos de los número no es mayor de 10")

suma_digitos(var_1, var_2)

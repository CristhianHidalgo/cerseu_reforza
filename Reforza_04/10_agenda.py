
nombre = input("Ingrese el nombre del usuario: ")
nombre = nombre.capitalize()
apellido = input("Ingrese el apellido del usuario: ")
apellido = apellido.capitalize()
edad = input("Ingrese la edad del usuario: ")


file = open("ficheros/agenda.txt", "a+")
file.write(nombre + "," + apellido + "," + edad + "\n")

file = open("ficheros/agenda.txt", "r")
print(file.read())

file.close()
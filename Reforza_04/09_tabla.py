
while True:
    try:
        num = int(input("Ingrese un número entero entre 1 y 20: "))
        break
    except ValueError:
        print("Error: Ingrese un número entero")

if num < 1 or num > 20:
    print("El número es menor que 1 o mayor que 20")
else:
    file = open("ficheros/tabla.txt", "a+")
    file = open("ficheros/tabla.txt", "w")
    for i in range(1, 13):
        mult = num * i
        file.writelines(f"{num} x {i} = {mult}\n")
    file = open("ficheros/tabla.txt", "r")
    print(file.read())
    file.close()

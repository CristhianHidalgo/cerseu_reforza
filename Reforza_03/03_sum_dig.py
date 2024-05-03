
num = int(input("Ingrese un numero: "))
dig_num = []

for i in str(num):
    dig_num.append(int(i))

def sum_dig(num):
    return sum(dig_num)

print(f"La suma de los dígitos del número es: {sum_dig(num)}")
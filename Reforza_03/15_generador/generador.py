

def leer_numero():
    ini = int(input("Ingrese el menor numero: "))
    fin = int(input("Ingrese el mayor numero: "))
    return {"var_1": ini, "var_2": fin}

def generador():
    variables = leer_numero()
    lista = []
    for i in range(variables["var_1"], variables["var_2"] + 1):
        lista.append(pow(i, 2))
    return lista
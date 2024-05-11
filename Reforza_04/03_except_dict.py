
persona = {"nombre": "Xavier", "apellido": "Rodriguez", "dni": "63325345"}


def funcion_3(persona):
    try:
        persona["profesion"]
    except KeyError:
        print("Error: El key 'profesion' no existe en el diccionario")


funcion_3(persona)

# Ejercicio 5

def validar_usuario(usuario):
    if len(usuario) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres"
    elif len(usuario) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    elif usuario.isalnum() == False:
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True
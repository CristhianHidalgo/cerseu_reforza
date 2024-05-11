
import requests as rq

var_res = rq.get("https://jsonplaceholder.typicode.com/users")

var_json = var_res.json()

user_1 = var_json[0]

nombre_1 = user_1["name"]
correo_1 = user_1["email"]
nombre_compañia_1 = user_1["company"]["name"]
nombre_web_1 = user_1["website"]

print(f"Bienvenido {nombre_1}. El correo que nos proporcionó"
      f" es {correo_1} y la compañia actual donde trabaja se"
      f" llama {nombre_compañia_1}. Dentro de sus datos también"
      f" encontramos una website que es: {nombre_web_1}")

var_json.append({"id": 11, "nombre": "Fernando", "apellido": "Rodriguez",
                 "edad": 32, "compañia": "Transportes Gechiza"})

usuario_new = var_json[10]
print(f"Los datos del usuario nuevo son: {usuario_new}")

from Dicionario import Registro_clients
from Funciones_error import error_string

# Diccionario de productos de el menu


id = int(input("Ingrese su ID: "))
nombre = error_string("Ingrese el nombre: ")
correo = input("Ingrese el correo: ")

Registro_clients[id] = id
Registro_clients["nombre"] = nombre
Registro_clients["correo"] = correo

print(Registro_clients)
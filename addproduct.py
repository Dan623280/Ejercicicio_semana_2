from ast import Return

from Dicionario import Registro_products
from Funciones_error import error_string
from id import id_tabla

# Diccionario de productos de el menu
def registro_productos():

    id_usuario = id_tabla(3)
    nombre = error_string("el nombre: ")
    precio = int(input("Precio: "))

    

    #Registro_products["id"] = id_usuario
    #Registro_products["nombre"] = nombre
    #Registro_products["precio"] = precio
 
    return {
    "id" : id_usuario,
    "nombre" : nombre,
    "precio" : precio
}

registro_productos()
print(registro_productos(Registro_products))











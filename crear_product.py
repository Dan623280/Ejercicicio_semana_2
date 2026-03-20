from id import id_tabla
from diccionario import pedidos

from Funciones_error import error_string, error_number_int, error_number_float

def crear_product():

    cliente = error_string("nombre del cliente: ")
    producto = error_string("nombre del producto: ")
    cantidad = error_number_int("agregue la cantidad: ")
    precio = error_number_float("coloque el precio: ")

    pedidos[id_tabla(1)] = {"cliente": cliente, "producto": producto, "cantidad": cantidad, "precio": precio}  



# Echo por Luis Mario Suarez
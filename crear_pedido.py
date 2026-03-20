from id import id_tabla
from Dicionario import pedidos

from Funciones_error import error_string, error_number_int, error_number_float

def crear_pedido():

    cliente = error_string("nombre del cliente: ")
    producto = error_string("nombre del producto: ")
    cantidad = error_number_int("agregue la cantidad: ")
    precio = error_number_int("coloque el precio_unitario: ")
    precio_total = cantidad * precio
    pedidos[id_tabla(pedidos)] = {"cliente": cliente, "producto": producto, "cantidad": cantidad, "precio_unitario": precio, "precio_total": precio_total}  

    print("")
    print("Registro actualizado exitiosamente")
    print(f"cliente: {cliente}")
    print(f"producto: {producto}")
    print(f"cantidad: {cantidad}")
    print(f"precio_unitario: {precio}")
    print(f"precio_total: {precio_total}")
    print("")



# Echo por Luis Mario Suarez

#from crear_pedido import crear_pedido
#importa el dicionario donde se almacenan los productos
from Dicionario import productos

#importa la funcion de error de texto
from Funciones_error import error_string

#importa la funcion que devuelve el id de la tabla
from id import id_tabla

# Diccionario de productos de el menu
def r_productos():

    id = id_tabla(productos)
    nombre = error_string("nombre producto: ")
    precio = error_string("Precio unitario: ")

    productos[id] = {"nombre_producto": nombre, "Precio_unitario": precio}

    print("")
    print("Registro actualizado exitiosamente")
    print(f"nombre_producto: {nombre}")
    print(f"Precio_unitario: {precio}")
    print("")

#para llamar
#from addproduct import r_productos
        











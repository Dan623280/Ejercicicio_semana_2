from Dicionario import clientes
from Funciones_error import error_string
from id import id_tabla

# Diccionario de productos de el menu
def r_clientes():

    id = id_tabla(clientes)
    nombre = error_string("nombre: ")
    correo = error_string("correo: ")

    clientes[id] = {"nombre": nombre, "correo": correo}

    print("")
    print("Registro actualizado exitiosamente")
    print(f"nombre: {nombre}")
    print(f"correo: {correo}")
    print("")

#para llamar
#from addClients import r_clientes
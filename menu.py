
from Funciones_error import error_number_int


def menu():

    print("\n---------Registrar venta----------")
    print("1.- Registrar cliente ")
    print("2.- Regristrar producto")
    print("3.- Crear pedido")
    print("4.- Consultar pedido")
    print("5.- mostrar total de ingresos")
    print("6.- Generar reportes")
    print("7.- Salir")
    print("\n-----------------------")

    opcion = error_number_int("una opcion: ")
    return opcion

#para llamar
#from menu import menu
#Menu from menu import menu_principal()

from Funciones_error import error_number_int

#-------------------------------------------------
# Menu
#-------------------------------------------------

def menu_principal():
    
    #Dicionario
    print("")
    print("1. Agregar producto")
    print("2. Mostrar inventario")
    print("3. Calcular estadísticas")
    print("4. Salir")
    print("")

    # Preguntar Opcion a elegir
    pregunta = error_number_int("el numero de la acción que desea realizar: ")

    return pregunta





#importa los colores
from Color import verde,reset, rojo

#importa el menu
from menu import menu

#importa la fucion de registrar cliente
from addClients import r_clientes

#importa la funcion de registrar productos
from addproduct import r_productos

#importa la funcion de crear pedido
from crear_pedido import crear_pedido

#importa la funcion de pedido
from mostrar_pedido import pedido

#importa la funcion para calcular el total de ingresos
from calculo_ingreso import calculo_ingresos

#importa la funcion que trae los reportes
from Reporte import reporte

#variable de confirmacion
confir = "Y"

#ciclo de confirmacion
while confir == "Y": 

    #esta variable trae la funcion del menu y retorna el valor elegido por el usuario
    opcion =  menu()

    #verifica si el usuario eligio la opcion 1
    if opcion ==1:
        
        #se invoca la funcion para registrar los clientes
        r_clientes()

    #verifica si el usuario eligio la opcion 2
    elif opcion ==2:
        
        #se invoca la funcion para registrar los productos
        r_productos()

    #verifica si el usuario eligio la opcion 3
    elif opcion == 3:

        #se invoca la funcion para Crear los pedidos
        crear_pedido()

        
    #verifica si el usuario eligio la opcion 4
    elif opcion == 4:

        #se invoca la funcion que muestra los pedidos
        pedido()

    #verifica si el usuario eligio la opcion 5
    elif opcion == 5:
        
        #se trae el total de ingresos generados
        print(f"los ingresos obtenidos durante el dia: {calculo_ingresos()}")

    #verifica si el usuario eligio la opcion 6
    elif opcion == 6:

        #se imprime el reporte de los pedidos
        print("")
        print("Reporte")
        reporte()
        
    #verifica si el usuario eligio la opcion 6
    elif opcion == 7:

        #saca al usuario y le dice salida exitosa
        print(verde+"==================================================")
        print("=Salida exitosa Gracias por usar nuestro Programa=")
        print("=================================================="+reset)
        
        confir == "N"

    #si el usuario coloca un numero diferente al que esta en el menu ejecuta esta opcion
    else:

        #Mostar mensaje del numero no valido
        print(rojo+ "==================")
        print("=Numero no valido=")
        print("=================="+reset)
        
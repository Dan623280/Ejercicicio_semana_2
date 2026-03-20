
from menu import menu
from addClients import r_clientes
from addproduct import r_productos
from crear_pedido import crear_pedido
from mostrar_pedido import pedido
from calculo_ingreso import calculo_ingresos
from Reporte import reporte
while True: 

    opcion =  menu()



    if opcion ==1:
        
        r_clientes()

    elif opcion ==2:
        
        r_productos()

    elif opcion == 3:
        
        crear_pedido()

    elif opcion == 4:

        pedido()
        
    elif opcion == 5:
        
        print(f"los ingresos obtenidos durante el dia: {calculo_ingresos()}")

    elif opcion == 6:
        print("")
        print("Reporte")
        reporte()
        
    elif opcion == 7:

        break

    else:

        print("numero no valido")
        
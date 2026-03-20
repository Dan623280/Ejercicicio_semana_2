from Dicionario import registro_clientes
while True:
        print("\n---------Registrar venta----------")
        print("__________________________")
        print("1.- Registrar cliente ")
        print("__________________________")
        print("__________________________")
        print("2.- Regristrar producto")
        print("__________________________")
        print("_________________")
        print("3.- Crear pedido")
        print("_________________")
        print("______________________")
        print("4.- Consultar pedido")
        print("_____________________")
        print("____________________")
        print("5.- Generar reportes")
        print("____________________")
        print("------------")
        print("6.- Salir")
        print("------------")
        opcion = int(input("ingrese una opcion: "))
        
        print("\n-----------------------")
        
        if opcion ==1:
            cliente = input("ID del cliente: ")
            nombre = input("Nombre del cliente: ")
            correo = input("agregar correo: ")
        

        elif opcion ==2:
            nombre_producto = input("Agregar producto: ")
            precio = float(input("precio del producto: "))
            cantidad = int(input("agregar cantidad: "))

            total_pago = precio * cantidad
            print("total del pago.")

    

from Dicionario import Registro_clients
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
            nombre = input("agregar nombre: ")
            if nombre.replace(" ","").isalpha():
                print(Registro_clients)
                break
            else:
                print("Error: el nombre solo debe tener letras")

precio = float(input("agregue precio: "))
cantidad = int(input("agregue cantidad: "))      
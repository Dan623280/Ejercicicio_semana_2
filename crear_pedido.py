from id import id_tabla
from Dicionario import pedidos, productos,clientes
from verificacion import verificacion
from Funciones_error import error_string, error_number_int

def crear_pedido():

    listcliente = []
    listproducto = []

    for cliente in clientes.values():

        listcliente.append(cliente['nombre'])

    for product in productos.values():

   
        listproducto.append(product['nombre_producto'])

    confir_cli = "Y"
    confir_pro = "Y"
    while confir_cli == "Y":

        cliente = error_string("nombre del cliente: ")

        if  cliente not in listcliente:

            print(f"{cliente} no esta en la lista de Productos")

        else:

            confir_cli = "N"

    producto=""
    while confir_pro == "Y":

        producto = error_string("nombre del producto: ")

        if  producto not in listproducto:

            print(f"{producto} no esta en la lista de clientes")

        else:

            confir_pro = "N"
            
    
    cantidad = error_number_int("la cantidad: ")

    precio = 0


    for indivi_producto in productos.values():
        if indivi_producto['nombre_producto'] == producto:
            precio = indivi_producto['Precio_unitario']


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
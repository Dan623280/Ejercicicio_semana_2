from Dicionario import  pedidos
from calculo_ingreso import calculo_ingresos

def total_ingresos_total_pedidos():

    print("el total de pedidos registrados es: ",len(pedidos))

    print("el total de ingresos generados es: ",calculo_ingresos())

def pedidos_agrupados_y_productos():
    
    personas = []

    for pedido in pedidos.values():

        if pedido['cliente'] in personas:

            continue

        else:

            personas.append(pedido['cliente'])

    for persona in personas:

        print(f"Estos son los pedidos del cliente {persona}")

        for pedido in pedidos.values():

            if persona  == pedido['cliente']:

                print("")
                print(f"Producto: {pedido['producto']}")
                print(f"Cantidad: {pedido['cantidad']}")
                print(f"precio unitario: {pedido['precio_unitario']}")
                print(f"precio total: {pedido['precio_total']}")
                print("")

    productos_agrupados = []

    for pedido in pedidos.values():

        if pedido['producto'] in productos_agrupados:

            continue

        else:
            
            productos_agrupados.append(pedido['producto'])
    
    print("Estos son los productos vendidos durante el dia")

    for producto in productos_agrupados:

        print(f"Producto: {producto}")
    

def reporte():

    total_ingresos_total_pedidos()
    pedidos_agrupados_y_productos()


#para llamar
#from Reporte import total_ingresos_total_pedidos, pedidos_agrupados_y_productos, reporte

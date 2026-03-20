from Dicionario import pedidos

# mostrar pedidos
def pedido():
    for pedido, datos in pedidos.items():
        print(f"Pedido {pedido}")
        print("Cliente:", datos["cliente"])
        print("Producto:", datos["producto"])
        print("Cantidad:", datos["cantidad"])
        print("Precio:", datos["precio_unitario"])
        print("Total:", datos["precio_total"])
        print("---------------------")

# Echo por Luis Mario Suarez

#pra llamar
#from mostrar_pedido import pedido
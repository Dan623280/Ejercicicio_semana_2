from Dicionario import pedidos

# calcular total
def total_pago():
    for pedido, datos in pedidos.items():
        datos["total_pago"] = datos["cantidad"] * datos["precio"]

# mostrar pedidos
def pedido():
    for pedido, datos in pedidos.items():
        print(f"Pedido {pedido}")
        print("Cliente:", datos["cliente"])
        print("Producto:", datos["producto"])
        print("Cantidad:", datos["cantidad"])
        print("Precio:", datos["precio"])
        print("Total:", datos["total_pago"])
        print("---------------------")

# Echo por Luis Mario Suarez
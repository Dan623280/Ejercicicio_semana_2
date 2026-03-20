from Dicionario import registro_productos, registro_clientes, Pedido

def calculo_ingresos():
    total = 0
    for pedido_unitario in Pedido.values():

        total = total + pedido_unitario['Total_pedido']
        
    return total



#from Calculo import calculo_ingresos
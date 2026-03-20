from Dicionario import pedidos

def calculo_ingresos():

    total = 0

    for pedido_unitario in pedidos.values():

        total = total + pedido_unitario['precio']
        
    return total



#from Calculo import calculo_ingresos
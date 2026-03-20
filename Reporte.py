from Dicionario import registro_productos, registro_clientes, pedidos
from calculo_ingreso import calculo_ingresos
print("el total de pedidos registrados es: ",len(pedidos))
print("el total de ingresos generados es: ",calculo_ingresos())

def pedidos_agrupados():
    print("el numero de pedidos agrupados por cliente es: ",calculo_ingresos())
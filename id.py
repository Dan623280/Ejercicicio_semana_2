
from Dicionario import pedidos, Clientes, productos

def id_tabla(number):
    
    if number == 1:

        if len(pedidos) == 0:

            return 1
        
        else:

            return len(pedidos) +1
        
    elif number == 2:

        if len(Clientes) == 0:
            
            return 1
        
        else:

            return len(Clientes) +1
        
    elif number == 3:

        if len(productos) == 0:
            
            return 1
        
        else:

            return len(productos) +1
        
print(id_tabla())
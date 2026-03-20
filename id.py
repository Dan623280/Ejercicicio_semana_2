
from Dicionario import pedidos, registro_clientes, registro_productos
from Color import rojo, reset

def id_tabla(number):
    
    if number == 1:

        if len(pedidos) == 0:

            return 1
        
        else:

            return len(pedidos) +1
        
    elif number == 2:

        if len(registro_clientes) == 0:
            
            return 1
        
        else:

            return len(registro_clientes) +1
        
    elif number == 3:

        if len(registro_productos) == 0:
            
            return 1
        
        else:

            return len(registro_productos) + 1
    else:

            #mensaje numero no valido
            print(rojo + "==================")
            print("=Numero no valido=")
            print("=================="+reset)
        

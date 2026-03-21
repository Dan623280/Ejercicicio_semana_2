
from Dicionario import pedidos

def verificacion(valor, lista):

    while True:

        if  valor not in lista:

            print("cliente no esta en la lista de clientes")

        else:

            return valor
    
#from verificacion import verificacion
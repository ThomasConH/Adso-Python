#raise-IndexError
#assert

def Indicelista(lista,indice):
    try:
        lista=lista[indice]
        print('lista')
    except IndexError:
        print('error de indice')
    
lst=[]
ind=2
Indicelista(lst,ind)
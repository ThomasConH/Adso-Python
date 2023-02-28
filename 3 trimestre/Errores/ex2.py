#ValueError

def cambio(lista,c1,c2,c3,c4,c5):
    try:
        lista
        c1,c2,c3,c4,c5=lista
        print(c1,c2,c3,c4,c5)
    except ValueError:
        print('los elementos de la lista no cumplen con los parametros')






lista=[1,2,3,4]
a=None
b=None
c=None
d=None
e=None
cambio(lista,a,b,c,d,e)
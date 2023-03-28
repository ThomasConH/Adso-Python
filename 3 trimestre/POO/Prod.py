class Venta:
    contador = 0
    def __init__(self, producto, precio):
        self.__producto = producto
        self.__precio = precio
        Venta.contador+=1
        
    def getProducto(self):
        Venta.contador+=1
        return self.__producto
        
    def setProducto (self,producto):
        self.__producto = producto
        Venta.contador+=1
    
    def getPrecio (self):
        return self.__precio

    def setPrecio (self,precio):
        self.__precio = precio
        Venta.contador+=1
    
    def getIva (self):
        self.__precio
        iva = self.__precio * 0.19
        Venta.contador+=1
        return iva

    

ob = Venta("Mouse",15000)
ob = Venta("Teclado",13000)
print("El valor de",ob.getProducto(),"es de",ob.getPrecio())
print("El iva del producto es de:",ob.getIva())
print(ob.contador)


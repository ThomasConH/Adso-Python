class Persona:
    def __init__(self,nombre,id):
        self.__nombre=nombre,id
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre
    
    def GetId(self):
        return self.__id

    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def SetId(self,id):
        self.___id = id

ob=Persona('Maria',123456)
print(ob.getNombre())
print(ob.GetId())
ob.setNombre('Ana',152432)
print(ob.getNombre())
print(ob.SetId())
#print(type(ob))

"""class Aprendiz(Persona):
    def __init__(self,nombre,ficha):
        Persona.__init__(self,nombre)
        self.__ficha=ficha

    def getFicha(self):
        return self.__ficha


app=Aprendiz('Pedro',12345)
print(app.getFicha())
print(app.getNombre())
print(app.getFicha())"""
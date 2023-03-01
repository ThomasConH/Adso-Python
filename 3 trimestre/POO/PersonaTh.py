class Persona:
    def __init__(self,nombre,cc):
        self.__nombre= nombre
        self.__cc = cc
        #print('Constructor Activado')        

    def getNombre(self):
        return self.__nombre, self.__cc
    
#    def Getcc(self):
#        return self.__cc

    def setPersona(self,nombre,cc):
        self.__nombre=nombre
        self.__cc = cc
    
#    def Setcc(self,cc):
#        self.___cc = cc

ob=Persona('Maria',123456)
print(ob.getNombre())
#print(ob.Getcc())
ob.setPersona("Ana",192732)
print(ob.getNombre())
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
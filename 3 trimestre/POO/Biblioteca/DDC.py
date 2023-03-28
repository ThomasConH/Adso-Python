class pedido:
    def __init__(self,Id_us,Titm,Idm):
        self.__Id_us = Id_us
        self.__Titm = Titm
        self.__Idm = Idm
    
    def getLibro(self):
        return self.__Titm,self.__Idm
    
    def setLibro(self,Titm,Idm):
        self.__Titm = Titm
        self.__Idm = Idm
    
    def getUsuario(self):
        return self.__Id_us
    
    def setUsuario(self,Id_us):
        self.__Id_us=Id_us
    
    

#ob = pedido(10293,"Satanas","2306")
#print("los datos del libro son:",ob.getLibro())
#print("Los datos del usuario son:",ob.getUsuario())

class producto(pedido):

    def __init__(self,Titm, TipoLib, Autor, Edit,Idm):
        super().__init__(self,Titm,Idm)
        self.__TipoLib = TipoLib
        self.__Autor = Autor
        self.__Edit = Edit

    def getGen(self):
        return "El genero del libro es:",self.__TipoLib
    
    def setGen(self,TipoLib):
        self.__TipoLib = TipoLib
    
    def getAutor(self):
        return "El/la autor(a) del libro es:",self.__Autor
    
    def setAutor(self,Autor):
        self.__Autor = Autor
    
    def getEdit(self):
        return "La editorial del libro es:", self.__Edit

    def setEdit(self,Edit):
        self.__Edit = Edit
    
    def datos(self):
        return "El nombre del libro es",super().getLibro()


"""oc = producto("Satanas", "Drama", "Mario Mendoza","PDLL", 12314 )
print(oc.datos())
print(oc.getAutor())
print(oc.getLibro())
print(oc.getEdit())"""

class Revista(pedido):
    def __init__(self,EdRev,Titm, Idm):
        super().__init__(self,Titm,Idm)
        self.__EdRev = EdRev
    
    def getEdic(self):
        return "La edicion de la revista es:",self.__EdRev

    def setEdic(self,EdRev):
        self.__EdRev = EdRev
    
    def datosRev(self):
        return "Los datos de la revista son:" ,super().getLibro()
    
"""rev = Revista(1785,"Vea",1209742)
print(rev.datosRev())
print(rev.getEdic())"""

class Lector:
    def __init__(self,nombre,Direccion,Telefono):
        self.__nombre = nombre
        self.__Direccion = Direccion
        self.__Telefono = Telefono
        self.__Libros = []
    
    def getNombre(self):
        return "El nombre de la persona que hizo el pedido es:",self.__nombre
    
    def setNombre(self,nombre):
        self.__nombre = nombre

    def getDireccion(self):
        return self.__Direccion
    
    def setDireccion(self,Direccion):
        self.__Direccion = Direccion
    
    def getTel(self):
        return self.__Telefono

    def setTel(self,Telefono):
        self.__Telefono = Telefono
    
    def agregarLib(self,Libro):
        self.__Libros.append(Libro)
    
    def verLibros(self):
        return self.__Libros
    
    def getDatosLec(self):
        return self.__Direccion, self.__nombre, self.__Telefono

"""Per = Lector("JH","Calle Bendicion", 40241)
Lib1 = pedido(2304,"Satanas",54017)
Lib2 = pedido(2304,"Hector Lavoe Biografia",60147)
Lib3 = pedido(2304,"Berserk",57148)

Per.agregarLib(Lib1)
Per.agregarLib(Lib2)
Per.agregarLib(Lib3)

for lectura in Per.verLibros():
    print(lectura.getLibro())"""

    
class Aprendiz(Lector):
    def __init__(self, nombre, Direccion, Telefono, Ficha):
        super().__init__(Direccion, Telefono, nombre)
        self.__Ficha = Ficha

    
    def getFicha(self):
        return "El numero del Curso es:",self.__Ficha

    def setFicha(self,Ficha):
        self.__Ficha = Ficha
    
    def datosLector(self):
        return "Los datos del estudiante son:" ,super().getDatosLec() 
        

"""Ap = Aprendiz("Jonathan","calle 13", 51475, 1102)
print(Ap.datosLector())
print(Ap.getFicha())"""

class Docente(Lector):
    def __init__(self, nombre, Direccion, Telefono, CC):
        super().__init__(Direccion, Telefono, nombre) 
        self.__CC = CC

    
    def getCC(self):
        return "El numero de cedula deldocente es es:",self.__CC

    def setCC(self,CC):
        self.__CC = CC
    
    def datosLector(self):
        return "Los datos del Docente son:" ,super().getDatosLec()
    
"""Doc = Docente("Jojo","Calle 24",3024842,1254787)
print(Doc.datosLector())                                   
print(Doc.getCC())"""         

class Bibliotecario:
    def __init__(self,Idbi,nombrebi):
        self.__Idbi = Idbi
        self.__nombrebi = nombrebi
    
    def getIdBi(self):
        return self.__Idbi
    
    def setIdBi(self,Idbi):
        self.__Idbi = Idbi
    
    def getNombrebi(self):
        return "El bibliotecario que lo atendera es:",self.__nombrebi
    
    def setNombrebi(self,nombrebi):
        self.__nombrebi = nombrebi

    def getDatosbi(self):
        return "Los datos del bibliotecario que lo atendera son:",self.__nombrebi,self.__Idbi

"""bib = Bibliotecario(182733,"Andres")
Per = Lector("Jolyne","Calle 13", 65847)
Lib1 = pedido(2458,"Apocalipsis",1458)
Lib2 = pedido(2458,"Jojos Bizarre Adventure",3657)
Lib3 = pedido(2458,"Berserk",8547)

Per.agregarLib(Lib1)
Per.agregarLib(Lib2)
Per.agregarLib(Lib3)

for lectura in Per.verLibros():
    print(lectura.getLibro(), bib.getDatosbi())"""


    

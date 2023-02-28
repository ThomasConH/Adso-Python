class Persona: #Define la clase con nombre "Persona"
    def __init__(self,nombre): # Crea la funcion con __init__ para inicializar el objeto dentro de la clase y los parametros self y nombre
        #Self es la palabra que indica que la funcion pertenece a la clase definida
        self.__nombre=nombre #Asigna __nombre para que la cadena que contiene el nombre se vuelva privado y oculto para la vista del publico
        #print('Constructor Activado')   

    def getNombre(self): #Crea la funcion GetNombre con el parametro self 
        return self.__nombre #Mostrara el nombre, mas no se podra cambiar

    def setNombre(self,nombre):#Creara otra funcion con parametro self y nombre
        self.__nombre=nombre #Cambiara el nombre por el establecido abajo

ob=Persona('Maria') #Establece que la clase persona sea "ob" y el nombre sea "maria"
print(ob.getNombre()) #Imprime la funcion getnombre ligada a ob
ob.setNombre('Ana') #cambia el nombre de setnombre a "ana"
print(ob.getNombre())#imprime la funcion getnombre con el nombre cambiado
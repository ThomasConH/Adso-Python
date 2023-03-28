class Vehiculo: #Crea clase con nombre vehiculo
    
    def __init__(self,tipo): #Inicia el constructor con los atributos self y tipo
        self.tipo=tipo #Define el parametro tipo de manera publica
    
    def descripcion(self): #Crea un metodo con nombre descripcion
        print('Soy generico no tengo descripcion',self.tipo) #Al invocar el metodo descripcion, genera el print, y invoca el tipo de vehiculo
#v=Vehiculo('Cualquier tipo')

    def getTipo(self): #Crea el metodo getTipo para invocar el tipo de vehiculo
        return self.tipo #retorna el tipo de vehiculo
        #return Vehiculo.tipo
    
    def __str__(self): #Sobreescribe la funcion __str__ para que retorne en que clase esta el objeto
        return 'Soy objeto de la clase Vehiculo' #Cuando se ponga el print, imprimira el retorno

class Herramienta:#Crea la clase herramienta
    def __init__(self,proposito): #Inicia el constructor con el parametro self y el parametro proposito
        self.__proposito=proposito #Define el proposito de manera privada
    
    def getProposito(self): #Crea el metodo getProposito para que imprima el proposito
        return self.__proposito #Retorna el anterior definido proposito
    
    def __str__(self): #Sobreescribe la funcion __str__ para que retorne donde esta el objeto
        return 'Soy objeto de la clase Herramienta' #Se imprimira el retorno cuando se invoque con un print

class Terrestre(Vehiculo,Herramienta): #Crea la subclase Terrestre, con la herencia de vehiculo y herramienta
    
    def __init__(self,tipo,proposito): #Inicia el constructor con los parametros self, tipo y proposito
        Herramienta.__init__(self,proposito) #Inicia el constructor de herramienta con el parametro proposito
        Vehiculo.__init__(self,tipo)        #Inicia el constructor de Vehiculo con el parametro tipo
    
    def datos(self): #Inicia el metodo datos con el parametro self
        print('Tipo: ',super().getTipo()) #El super identifica la clase padre donde esta ubicada getTIpo de manera que imprima el mismo tipo de vehiculo
        print('Tipo: ',super().getProposito())# El super identifica la clase padre donde esta ubicada getProposito donde muestra el proposito del vehiculo
    # def __str__(self):
    #     return 'Soy objeto de la clase Terrestre'
               
t=Terrestre("terrestre","carga") #Se define el tipo de vehiculo y el proposito del vehiculo
t.datos()
print(t.__str__())

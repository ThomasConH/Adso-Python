class ejemplo:
    
    
    def Instancia(self):
        return"Bruh pero en metodo de instancia"
    
    @classmethod
    def Clase(cls):
        return"Bruh pero en metodo de clase"
    
    @staticmethod
    def estatico():
        return"Bruh pero en metodo estatico"

Que = ejemplo()

print(Que.Instancia())
print(Que.Clase())
print(Que.estatico())

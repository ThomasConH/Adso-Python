#atributos de instancia

class usuario:
    def __init__(self,username,email):
        self.__username = username
        self.__email = email

    def getUsername(self):
        return self.__username
    
    def getEmail(self):
        return self.__email
    
    def setPersona(self,username,email):
        self.__username = username
        self.__email = email


red = usuario("Thomas","akjshdkjash@gmail.com")
print(red.getEmail())
print(red.getUsername())
print("--------------------------")
red.setPersona("Steezuz","alksjdljkajsf@gmail.com")
print(red.getEmail())
print(red.getUsername())
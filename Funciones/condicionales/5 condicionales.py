
num1 = int(input("digite el primer numero: "))
num2 = int(input("digite el segundo numero: "))
num3 = int(input("digite el tercer numero: "))

def par1(num1):    
    if num1 %2 == 0:
        return "el primer numero es par"
    else:
        return "el primer numero no es par"
def par2(num2):
    if num2 %2 == 0:
        return "El segundo numero es par"
    else:
        return "El segundo numero no es par"
def par3(num3):
    if num3 %2 == 0:
        return "el tercer numero es par"
    else:
        return "el tercer numero no es par"



print(par1(num1))
print(par2(num2))
print(par3(num3))
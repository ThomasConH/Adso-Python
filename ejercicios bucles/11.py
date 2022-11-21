a = 1 
q = 0 
num1 = int(input('ingrese el dividendo'))
num2 = int(input('ingrese el divisor'))
if (num1>= num2):
    while((num1 - num2)>=q):
        q = num2*a
        a = a +1
        print('el cociente es '+str(a-1)+' y el residuo es '+str((num1-q)))
else:
    print('el dividendo dede ser menor') 
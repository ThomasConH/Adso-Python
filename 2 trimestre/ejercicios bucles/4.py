for num in range(1,100):
    
    if num > 1:
        cont=0
        i=2
        while i<num and cont==0:
            resto=num%i
            #print("{} % {} = {}" .format(num, i, resto))
            if resto==0:
                cont+=1
            i+=1
        if cont==0:
            print(num)
            

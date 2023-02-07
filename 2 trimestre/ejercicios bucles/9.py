x=int(("ponga la base: "))
y=int(input("ponga exponente: "))
i=1 
opera=x
while(i<y):
    i+=1
    opera*=x
if y<=0:
    opera=1
print(opera)

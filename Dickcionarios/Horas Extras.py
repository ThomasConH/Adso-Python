Horas_Extras = {}

while True:
    name = input("Ingrese el nombre del empleado : ")
    if name == '':
        break
    
    score = int(input("Ingrese las horas de laburo (0 - 8): "))
    if score not in range(0, 9):
	    break
    
if name in Horas_Extras:
        Horas_Extras[name] += (score,)
else:
        Horas_Extras[name] = (score,)
        
for name in sorted(Horas_Extras.keys()):
    adding = 0
    counter = 0
    for score in Horas_Extras[name]:
        adding += score
        counter += 1
    print(name, ":", adding * 5000)
import calendar

#Modulo calendar

#Primero, para hacer uso del modulo. Como muchos modulos hay que importarlo

#El modulo calendar es un modulo de tiempo que esta almacenado en la biblioteca de python, esta funcion, como bien se describe , es un modulo que relaciona las funciones relacionadas
#con el calendario, entre ellos esta mostrar el calendario, es decir que mostrara los dias de lunes a domingo, cabe recalcar que para hacer el calculo de los dias, cada dia tiene
#su determinado numero



# Lunes = 0
# Martes = 1
# Miercoles = 2
# Jueves = 3
# Viernes = 4
# Sabado = 5
# Domingo = 6

#El modulo hace una representacion del calendario en meses, donde se define que el mes 1 es Enero y el mes 12 es Diciembre
#La manera de invocar la funcion calendar es de la siguiente manera

#-------------------------------------
# print(calendar.calendar(2023))
#-------------------------------------

#Para invocar el modulo calendar sin necesidad del print, se pone "prcal" despues del punto intermedio

#-------------------------------------
# calendar.prcal(2023)
#-------------------------------------

#Es nacesario que despues de poner la funcion, se especifique el año que se invocara el calendario

#Tambien, si se necesita, es necesario indicar el mes del año que se esta invocando, esto despues de la funcion month

#-------------------------------------
# print(calendar.month(2007, 6))
#-------------------------------------

#Tambien puede hacerse uso de prmonth par invocarla sin necesidad de utilizar el print

#-------------------------------------
# calendar.prmonth(2007, 6)
#-------------------------------------

#En el modulo calendar, tenemos una funcion la cual nos permite mostrar el calendario, pero en vez de iniciar con el valor 0 (Lunes), puede empezar por el valor que uno quiera
#Esto con la funcion setfirstweekday(calendar."Nombre de dia")

#-------------------------------------
# calendar.setfirstweekday(calendar.THURSDAY)
# calendar.prmonth(2007, 6)
#-------------------------------------

#En el modulo calendar podemos encontrar la funcion weekday, es la funcion la cual nos sirve para buscar que dia de la semana es una fecha en especifico


#-------------------------------------
# a = print(calendar.weekday(2007,6,23))
#importante no usar 0 antes del mes
#Aqui imprimira 5 y para entender este valor hay que recordar la siguiente tabla:
# Lunes = 0
# Martes = 1
# Miercoles = 2
# Jueves = 3
# Viernes = 4
# Sabado = 5
# Domingo = 6
#---------------


#Tambien encontramos la funcion weekheader. Lo que hace esta funcion es determinar el numero de caracteres que quiere que se utilicen para el nombre de los dias de la semana

#---------------
# print(calendar.weekheader(2))
#Esta funcion lo que hace es que responda con solo las dos primeras letras del calendario en ingles
#Mo Tu We Th Fr Sa Su
# print(calendar.weekheader(4))
#El modulo solo detecta hasta el tercer caracter, despues de ese, el calendario no añade mas, sino que añade espacios, y los separa mas
#---------------


#La funcion isleap y leapdays tienen la funcion, detectan que años son bisiestos, el primero es para preguntar si determinado es bisiesto
#El segundo para dar un rango de años y preguntar cuantos de ellos fueron años bisiestos
#---------------
# print(calendar.isleap(2020)) #2020 fue año bisiesto
# print(calendar.leapdays(2010, 2021)) #Esto es desde 2010 hasta 2020 ya que no invluye el ultimo numero
#---------------


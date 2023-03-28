"""Para subir al git el codigo, hay que tener la base de datos en la misma carpeta que se va a subir :)"""

"""Select"""
# import sqlite3 #importa el paquete sqlite3

# con = sqlite3.connect("C:\\thomas\\sqlite-tools\\db\\persona.db") #conecta python con la base de datos de una determinada direccione

# print(type(con)) #muestra el tipo de objeto que se esta eecutando <class 'sqlite3.Connection'> es un objeto que viene de un paquete que se importo previamente

# micursor = con.cursor() #crea un cursor el cual servira para seleccionar las diferentes funciones que queremos que haga el codigo

# print(type(micursor))  #Muestra el tipo de objeto que es mi cursor

# new_Sql = "SELECT * from tb_persona;" #Crea la funcion que usara el SQL

# micursor.execute(new_Sql) #El cursor da la ordern de ejecutar la anterior funcion

# lista = micursor.fetchall()   #Pone dentro de una variable llamada lista todos los datos que se dieron en micursor

# for fila in lista: # Hara un bucle en donde se dara el valor fila, para cada linea de datos
#     print(fila[0]) # imprimira la primera fila, es decir el id
#     print(fila[1]) # imprimira el nombre
#     print(fila[2]) # imprimira el apellido
#     print(fila[3]) # imprimira el email
#     print("*"*10) # Hara un separador de 10 asteriscos por cada linea de datos de cada persona

#---------------------------------------------------------------------

"""Select con parametros"""
# import sqlite3 #importa el paquete sqlite3


# with sqlite3.connect("C:\\thomas\\sqlite-tools\\db\\persona.db") as base: #Relaciona el archivo de python con el archivo que esta en los parentesis
#     micursor = base.cursor() #Relaciona el nuevo cursor con el archivo "base"
#     order_sql = "SELECT first_name, id from tb_persona where id  >5;" #Da la orden de que se muestren los nombres de la tabla que estan con el id que sea mayor que 5
#     print(micursor.execute(order_sql).fetchall()) #Imprime la orden, y selecciona todos con el fetchall

#-------------------------------------------------------------------

"""Select con mas parametros y funciones"""

# import sqlite3 #importa el paquete sqlite3

# con = sqlite3.connect("C:\\thomas\\sqlite-tools\\db\\persona.db") #Conecta el archivo python con el archivo en el parentesis

# micursor = con.cursor() #crea un cursor el cual servira para seleccionar las diferentes funciones que queremos que haga el codigo

# def select (tabla, campo, operador, dato): #Hace una funcion con los parametros tabla, campo, operador y dato
#     sentencia = f"SELECT * FROM {tabla} WHERE {campo} {operador} '{dato}'" #Da la orden con cada uno de los datos que se hicieron dentro de los corchetes
#     lista = micursor.execute(sentencia) #Crea una variable con la orden que se le dio al cursor  y este tiene la orden que esta en la sentencia
#     return lista.fetchall() #Retorna la orden dando todos los campos con fetchall

# print(select("tb_persona", "id", ">", "20"))

#-------------------------------------------------------------------

"""Update"""

import sqlite3 #importa el paquete sqlite3

def modificar (tabla, campo, dato, id):
    sentencia = f"UPDATE"
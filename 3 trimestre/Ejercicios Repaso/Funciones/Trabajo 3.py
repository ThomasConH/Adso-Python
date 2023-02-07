#calcular el maximo de numeros positivos introducidos por teclado,sabiendo que metemos numeros hasta que introduzcamos uno negativo. El negativo no cuenta.



def negpo ():
    Jugando = True
    conta = 0
    while Jugando:
        conta += 1
        trie = int(input(print("Ingrese el numero: ")))
        if trie < 0:
            print("Usted utilizo", conta, "intentos")
            Jugando = False
        elif trie >= 0:
            print("Siga intentando")
            print("Llevas", conta, "intentos")


 

        
negpo()
def excepcion1():
    try:
        arc = open("archivo.txt")
    except FileNotFoundError:
        print("Ese archivo no esta :c")

#excepcion1()

def excepcion2():
    try:
        import bladeR
    except ImportError:
        print("No hay un modulo con ese nombre parce")

#excepcion2()

def excepcion3():
    try:
        print(x)
    except NameError:
        print("Socio no entiendo que es x")


#excepcion3()
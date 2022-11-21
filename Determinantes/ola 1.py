secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

N = int(input("Dime el numero que quieres adivinar"))

while N != 777:
    print("Patico ese no es")
if N == 777:
    print("Salvao papa")
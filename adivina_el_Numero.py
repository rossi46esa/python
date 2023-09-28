secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")
num = int(input("Digite el número que considera es el elegido: "))

while num !=secret_number:
    if num != secret_number: print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    else:
        print("¡Bien hecho, muggle! Eres libre ahora.")
    num = int(input("Digite el número que considera es el elegido: "))
print("¡Bien hecho, muggle! Eres libre ahora.")

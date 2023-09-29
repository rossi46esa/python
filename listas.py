#Listas en Python
# Rosa Herrera - ESIT

numbers = [10, 5, 7, 2, 1]
print("Contenido de la lista original:", numbers)  # Imprimiendo el contenido de la lista original.

numbers[0] = 111
print("\nContenido de la lista con cambio:", numbers)  # Imprimiendo contenido de la lista con 111.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Contenido de la lista con intercambio:", numbers)  # Imprimiendo contenido de la lista con intercambio.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.

print(numbers) #también imprime la lista

#eliminando un elemento de la lista...
#del es una instrucción, NO una función.

del numbers[1]
print("imprimiendo lista - 1: ",len(numbers))
print(numbers)

#Al eliminar un elemento ya NO puedes acceder a ese valor, ni agregarle un valor.


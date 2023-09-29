#ejercicio beatles // listas
# Rosa Herrera - ESIT

# paso 1
beatles=[]
print("Paso 1:", beatles)

# paso 2
print("Paso 2:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
# paso 3
print("Paso 3:", beatles)
for i in range(2):
    valor = input("agrega más miembros de la banda: ")
    beatles.append(valor)
# paso 4
print("Paso 4:", beatles)
del beatles[-1]
del beatles[-1]
# paso 5
print("Paso 5:", beatles)
beatles.insert(0,"Ringo Starr")

# probando la longitud de la lista
print("Los Fav", len(beatles))
print(beatles)

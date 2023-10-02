# diccionarios Python
# Rosa Herrera - ESIT

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}
 
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

#para modificar un dato, por ejemplo, el del gato
dictionary['gato'] = 'minou'
print(dictionary)

#insertar un elemento mediante el método update()
dictionary2 = {"gato": "chat", "perro": "chien", "caballo": "cheval"}

dictionary2.update({"pato": "canard"})
print(dictionary2)

#eliminando un elemento
del dictionary['perro']
print(dictionary)

#Para eliminar el ultimo elemento de la
#lista, se puede emplear el método popitem():

dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
 
dictionary.popitem()
print(dictionary) # salida: {'gato': 'chat', 'perro': 'chien'}

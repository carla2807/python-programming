#Creo lista de frutas y numeros
fruits = ["apple","orange","pears","cherries","grapes"]

numbers = [3,"1998",2.5,987,"1994"]

print(fruits,numbers)

#append agrega elemento al final de la lista
fruits.append("peaches")
print(fruits)

#extend une al array fruits los numbers
fruits.extend(numbers)

print (fruits)

#remove elimina el elemento especifico, no importa la posicion de este
fruits.remove("grapes")
print (fruits)

#pop, elimina el primer elemento, elemento 0 .los arrays arrancan en 0
#pop(-1), eliminar el ultimo elemento, elemento 10
fruits.pop(0)
print(fruits)
fruits.pop(-1)
print(fruits)

#Para chequear si es V o F. Como "apple" no esta en la lista de fruits devuelve False
#el metodo count recibe como parametro "apple", devuelve 1 como resultado
#Comentar codigo desde array numbers hasta print(fruits) para que funcione
print("apple" in fruits)
print("apples" in fruits)
print(fruits.count("apple"))
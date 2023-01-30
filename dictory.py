#stuff es el diccionario
stuff = {"food": 15, "energy": 100, "enemies": 3 }

#get devuelve el valor de la key "food" que es 15
#print(stuff.get("food"))

#items devuelve lista ordernada completa --> dict_items([('food', 15), ('energy', 100), ('enemies', 3)])
#print(stuff.items())

#keys devuelve solo las keys --> dict_keys(['food', 'energy', 'enemies'])
#print(stuff.keys())

#print(stuff.popitem())
#print(stuff)

#creo diccionario new_items, el diccionario anterior que es stuff
#mediante update recibe como parametro el nuevo diccionario creado
#por medio de print se muestra actualizacion
new_items = {"rocks": 4, "arrows:":18}
stuff.update(new_items)
print(stuff)

#otro diccionario
new_items2 = {"torchs":2, "dragons":3}
stuff.update(new_items2)
print(stuff)
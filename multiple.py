#Creo clases Item y Germent que son las padres
class Item():
    def __init__(self, sku):
        # asigno el atributo
        self.sku = sku
   #Metodo print_Sku que accede a los atributos
    def print_sku(self):
        print("The sku is {}".format(self.sku))

class Garment():
    def __init__(self, section,type):
        # asigno los atributos
        self.section = section
        self.type = type
    #Metodo print_garment que accede a los atributos
    def print_garment(self):
        print("The garment is {} {}".format(self.section,self.type))

#Creo clase Shirts que es la hija y hereda
#referencia a las clases padres
class Shirts(Item,Garment):
    def __init__(self, sku, section, type, name, color):
        # asigno los atributos propios de la clase hija solamente
        self.name = name
        self.color = color
#inicializar los atributos de las clases padres
        Item.__init__(self, sku)
        Garment.__init__(self,section, type)

    def print_shirts(self):
        print("{} {} on sale!".format(self.name,self.color))

#Creo objeto Blouse, le asigno la clase y le paso atributos que elijo que deben ser 5
Blouse = Shirts("00001",43,"Tops","Formal Blouse","Red")

#El objeto Blouse accede a los 3 metodos: los de las clases que herada y su propio metodo
Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirts()

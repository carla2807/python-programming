#Los metodos son funciones
# Como creo clase? class Nombredelaclase
# Defino metodo constructor y los atributos def __init__(self, atributo1,atributo2,atributo3,etc..)

class Persona:
    def __init__(self,firstname,lastname,health,status):
#defino que los atributos firstname, lastname,health y status seran firstname,lastname,health,status
#Siempre uso self para asignarle a los atributos la instancia
        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

#defino metodo introduce
# self va para poder acceder a los atributos
    def introduce(self):
        print("My name is {} {} ".format(self.firstname,self.lastname))

#Creo objeto Maria(instanciar clase) que almacena clase Persona
# Maria llama al metodo introduce para mostrar el nombre y apellido
Maria = Persona("Maria","Gutierrez",95,"ok")
Maria.introduce()

#Herencia
#Creo clase Enemy y hereda como parametro la clase Persona, va entre parentesis
#Defino metodo constructor y los atributos def __init__(self, atributo1,atributo2,atributo3,etc..)

class Enemy(Persona):
    def __init__(self,firstname,lastname,health,status,weapon):
        #super permite heredar e inicializar los atributos de la clase Persona
        super().__init__(firstname,lastname,health,status)

        # defino que el atributo weapon sera weapon
        self.weapon = weapon

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10

        print(other.health)
    #Polimorfismo --> sobreescribe metodo introduce de la clase Persona
    #def introduce(self):
        #print("You are mortal")
#Creo objeto Alex(instancia clase) que almacena la clase Enemy
#Alex llama al metodo hurt y como parametro llama a objeto Maria
Alex = Enemy('Alex','Wayne',75, 'ok', 'rock')
Alex.hurt(Maria)
#Alex.introduce()













#HERENCIA DE PYTHON
class Persona:
    nombre   = str
    apellido = str
    edad     = int
    def __init__(self, nombre, apellido, edad) :
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
    
    def conversar(self,otra_persona):
        return f'Hola{otra_persona.nombre}, me llamo {self.apellido}, tengo {self.edad}'
    
class Hijo(Persona):
    ciudad  = str
    
    def __init__(self, nombre, apellido, edad, ciudad):
        super().__init__(nombre, apellido, edad)
        self.ciudad = ciudad
        
padre = Persona("Victor", "Grados", 40)
print(vars(padre))

hijo = Hijo("Elena", "Grados", 24, "Quito") 

print(vars(hijo))
print(padre.conversar(hijo))

#AGREGAR METODOS EN LA HERENCIA

class Persona2:

    nombre   = str
    apellido = str
   
    def __init__(self, nombre, apellido) :
        self.nombre   = nombre
        self.apellido = apellido
        
    
    def conversar(self, otra_persona):
        return f"Hola{otra_persona.nombre}, me llamo {self.apellido}, tengo {self.edad} "

class Hijo2(Persona2):
    estudios      = str
    lugarEstudios = str
    
    def __init__(self, nombre, apellido, estudios, lugardeestudios):
        super().__init__(nombre, apellido)
        self.estudios = estudios
        self.lugarEstudios = lugardeestudios
        
    def informar(self, otra_persona):
        return f'Buenas tardes,  {otra_persona.nombre} acabo de estudiar {self.estudios} en {self.lugarEstudios}'
    
padre2 = Persona2("Juan", "Flores")
hijo2  = Hijo2("Jose", "Perez", "Programacion", "YAVIRAC")


print(hijo2.informar(padre2))

class Padre:
     nombre = str
     apellido = str
     edad = int
     ciudad = str
    
     def __init__(self, nombre, apellido, edad, ciudad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad
        self. ciudad  = ciudad
        
     def bienvenido(self, hijo):
        return f'Buena {hijo.nombre} bienvenido a casa, la cena esta  en el micro yo me encunetro de viaje en  {self.ciudad} att: {self.nombre} {self.apellido}'
class Persona:
    nombre   = str
    apellido = str
    edad     = int
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre    
        self.apellido = apellido
        self.edad     = edad
        
if __name__ == '__main__':
    Alisson = Persona("Alisson", "Cumbajin", "21")
    Lenin = Persona("Lenin", "Montalvo", "19")
    
    print(vars(Alisson))
    print(vars(Lenin))
    
#La Funciòn __str__ Definir el string que se imprime



class Persona2:
    nombre   = str
    apellido = str
    edad     = int
    carrera  = str
    
    def __init__(self, nombre, apellido, edad, carrera):
        self.nombre   = nombre    
        self.apellido = apellido
        self.edad     = edad
        self.carrera  = carrera
        
    def __str__(self):
        return f"Hola me llamo" 
    
ejemplo1 = Persona2("Diego","Yanez", 29, "Desarrollo de Software")
ejemplo2 = Persona2("Sebastiàn","Navas", 29,"Marketing")
ejemplo3 = Persona2("Enzo","Guachilema", 29,"Diseño de modas")


print(ejemplo1)
print(ejemplo2)


def bu4(self):
    print("Hola"+ self.nombre + "Bienvenido a la carrera de "+ self.carrera)
        
ejemplo4 = Persona2("Diego","Yanez", 29, "Desarrollo de Software")
ejemplo5 = Persona2("Sebastiàn","Navas", 29,"Marketing")
ejemplo6 = Persona2("Enzo","Guachilema", 29,"Diseño de modas", "2")

ejemplo4.bienvenido()
ejemplo5.bienvenido()
ejemplo6.bienvenido()  


class Persona:
    nombre   = str
    apellido = str
    edad     = int 
    
    def __init__(self, nombre, apellido, edad):
        self.nombre   = nombre
        self.apellido = apellido
        self.edad     = edad  
        
    def saludar(self,otra_persona):
        return f"Hola", {otra_persona.nombre}, "me llamo " ,{self.nombre}
    
persona1 = Persona("Jordan", "Gonzales",22)
persona2 = Persona("Enzo", "Quishpe",20)

print(persona1.conversar(persona2))
print(persona1.conversar(Alisson))
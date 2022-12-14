from Padre import Persona
from Padre import Persona2
from Madre import Madre
from Padre import Padre

class Hijo3(Persona):
    vivienda = str
    
    def __init__(self, nombre, apellido, edad, vivienda):
        super().__init__(nombre, apellido, edad)
        self.vivienda = vivienda
        
hijo3 = Hijo3("Diego", "Yanes", 29, "Centro")
padre3 = Persona("german", "Yanes", 55)

print(vars(hijo3))
print(vars(padre3))

print(hijo3.conversar(padre3))

class Hijo4(Persona2):
    edad     = int
    semestre = str
    
    def __init__(self, nombre, apellido, edad, semestre):
        super().__init__(nombre, apellido)
        self.edad     = edad
        self.semestre = semestre
        
    def felicitar(self, padre):
        return f'Felicidades {self.nombre}, acabas de terminar tu {self.semestre}, a tu {self.edad} años. att tu {padre.nombre}'
    
padre4 = Persona2("Ivan", "Borja")
hijo4 = Hijo4("Ivan", "Borja", 23, "Quinto")

print(vars(padre4))
print(vars(hijo4))

print(hijo4.felicitar(padre4))

class Hijofinal(Padre, Madre):
    nombre   = str
    apellidoPaterno = str
    apellidoMaterno = str
    madre = Madre("", "", "", "")
    
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, edad, ciudad, madre):
        super().__init__(nombre, edad, ciudad)
        
        self.apellidoPaerno  = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.madre           = madre
        
padrefinal = Padre("GERMAN", "YANEZ", 56, "QUITO")
madrefinal = Madre("VERNONICA", "YANES", 56, "QUITO")
hijofinal  = Hijofinal("DIEGO", "YANEZ", "PEREZ", 29, "QUITO", Madre("VERNONICA", "YANES", 56, "QUITO"))

print(vars(padrefinal))
print(vars(madrefinal))
print(vars(hijofinal))
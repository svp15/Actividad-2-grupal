class Persona:
    def __init__(self, nombre, apellidos, numerodedocumentodeidentidad, añodenacimiento, paisdenacimiento, genero):
        self.nombre=nombre
        self.apellidos=apellidos
        self.numerodedocumentodeidentidad=numerodedocumentodeidentidad
        self.añodenacimiento=añodenacimiento
        self.paisdenacimiento=paisdenacimiento
        self.genero=genero

    def imprimir(self):
        print(f"Nombre = {self.nombre}")
        print(f"Apellidos = {self.apellidos}")
        print(f"Número de documento de identidad = {self.numerodedocumentodeidentidad}")
        print(f"Año de nacimiento = {self.añodenacimiento}")
        print(f"País de nacimiento = {self.paisdenacimiento}")
        print(f"Género = {self.genero}")
        print()

def datos():
    nombre=input("Ingrese el nombre: ")
    apellidos=input("Ingrese los apellidos: ")
    numerodedocumentodeidentidad=input("Ingrese el número de documento de identidad: ")
    añodenacimiento=int(input("Ingrese el año de nacimiento: "))
    paisdenacimiento=input("Ingrese el país de nacimiento: ")
    genero=input("Ingrese el género (H/M): ")
    if genero=="H":
        genero="Hombre"
    else:
        genero="Mujer"
    print()
    return Persona(nombre, apellidos, numerodedocumentodeidentidad, añodenacimiento, paisdenacimiento, genero)

p1=datos()
p2=datos()
p1.imprimir()
p2.imprimir()

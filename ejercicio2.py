class Planeta:
    def __init__(self, nombre, satelites, masa, volumen, diametro, distanciaalsol, tipo, esobservable, periodoorbital, periodorotacion):
        self.nombre=nombre
        self.satelites=satelites
        self.masa=masa
        self.volumen=volumen
        self.diametro=diametro
        self.distanciaalsol=distanciaalsol
        self.tipo=tipo
        self.esobservable=esobservable
        self.periodoorbital=periodoorbital
        self.periodorotacion=periodorotacion

    def imprimir(self):
        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distanciaalsol}")
        print(f"Tipo de planeta = {self.tipo}")
        print(f"Es observable = {self.esobservable}")
        print(f"Densidad del planeta = {self.calculardensidad()}")
        print(f"Es planeta exterior = {self.sabersiesplanetaexterior()}")
        print(f"El periodo orbital del planeta es = {self.periodoorbital}")
        print(f"El periodo de rotación del planeta es = {self.periodorotacion}")
        print()

    def calculardensidad(self):
        densidad=self.masa/self.volumen
        return densidad
    
    def sabersiesplanetaexterior(self):
        if self.distanciaalsol>3.4*149597870:
            return True
        else:
            return False

def datos():
    nombre=input("Ingrese el nombre del planeta: ")
    satelites=int(input("Ingrese la cantidad de satélites: "))
    masa=float(input("Ingrese la masa del planeta (kilogramos): "))
    volumen=float(input("Ingrese el volumen del planeta (kilómetros): "))
    diametro=int(input("Ingrese el diámetro del planeta (kilómetros): "))
    distanciaalsol=int(input("Ingrese la distancia media al sol (kilómetros): "))
    tipo=input("Tipo de planeta de acuerdo a su tamaño (gaseoso/terrestre/enano): ")
    esobservable=input("¿Es observable a simple vista? (si/no): ")=="si"
    periodoorbital=int(input("Ingrese el periodo orbital del planeta (años): "))
    periodorotacion=int(input("Ingrese el periodo de rotación del planeta (días): "))
    print()
    return Planeta(nombre, satelites, masa, volumen, diametro, distanciaalsol, tipo, esobservable, periodoorbital, periodorotacion)

p1=datos()
p2=datos()
p1.imprimir()
p2.imprimir()

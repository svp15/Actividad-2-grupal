class Automovil:
    def __init__(self, marca, modelo, motor, tipodecombustible, tipodeautomovil, puertas, asientos, velocidadmaxima, color, velocidadactual, esautomatico):
        self.marca=marca
        self.modelo=modelo
        self.motor=motor
        self.tipodecombustible=tipodecombustible
        self.tipodeautomovil=tipodeautomovil
        self.puertas=puertas
        self.asientos=asientos
        self.velocidadmaxima=velocidadmaxima
        self.color=color
        self.velocidadactual=velocidadactual
        self.esautomatico=esautomatico
        self.multas=0

    def getvelocidadactual(self):
        print(f"Velocidad actual: {self.velocidadactual}")

    def setvelocidadactual(self, nuevavelocidad):
        if nuevavelocidad>self.velocidadmaxima:
            self.multas=self.multas+1
            print("No se puede acelerar más allá de la velocidad máxima permitida.")
        elif nuevavelocidad<0:
            print("No se puede desacelerar a una velocidad negativa.")
        else:
            self.velocidadactual=nuevavelocidad
            print(f"Velocidad actual: {self.velocidadactual}")

    def getesautomatico(self):
        if self.esautomatico==True:
            print("Es automático.")
        else:
            print("No es automático.")
    
    def setesautomatico(self, nuevarespuesta):
        if nuevarespuesta=="si":
            self.esautomatico=True
            print("El vehículo ahora es automático.")
        else:
            self.esautomatico=False
            print("El vehículo ya no es automático.")

    def acelerar(self, aumento):
        if self.velocidadactual+aumento>self.velocidadmaxima:
            self.multas=self.multas+1
            print("No se puede acelerar más allá de la velocidad máxima permitida.")
        else:
            self.velocidadactual=self.velocidadactual+aumento
            print(f"Velocidad actual: {self.velocidadactual}")

    def desacelerar(self, disminucion):
        if self.velocidadactual-disminucion<0:
            print("No se puede desacelerar a una velocidad negativa.")
        else:
            self.velocidadactual=self.velocidadactual-disminucion
            print(f"Velocidad actual: {self.velocidadactual}")

    def frenar(self):
        self.velocidadactual=0
        print(f"Velocidad actual: {self.velocidadactual}")

    def calculartiempodellegada(self, distancia):
        if self.velocidadactual!=0:
            tiempodellegada=distancia/self.velocidadactual
            print(f"El tiempo de llegada estimado en horas es: {tiempodellegada}")
        else:
            print("El vehículo no se está moviendo.")

    def sabersitienemultas(self):
        if self.multas>0:
            print("El vehiculo sí tiene multas.")
        else:
            print("El vehículo no tiene multas")

    def sabervalortotaldemultas(self):
        valortotaldemultas=self.multas*633200
        print(f"El valor total de las multas es: {valortotaldemultas}")

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipodecombustible}")
        print(f"Tipo de automóvil = {self.tipodeautomovil}")
        print(f"Número de puertas = {self.puertas}")
        print(f"Cantidad de asientos = {self.asientos}")
        print(f"Velocidad máxima = {self.velocidadmaxima}")
        print(f"Color = {self.color}")
        print(f"Velocidad actual = {self.velocidadactual}")
        print(f"Es automático = {self.esautomatico}")

def datos():
    marca=input("Ingrese la marca del automóvil: ")
    modelo=int(input("Ingrese el año de fabricación: "))
    motor=int(input("Ingrese el volumen del cilindraje del motor (litros): "))
    tipodecombustible=input("Ingrese el tipo de combustible (gasolina/bioetanol/diésel/biodiésel/gas natural): ")
    tipodeautomovil=input("Ingrese el tipo de automóvil (carro de ciudad/subcompacto/compacto/familiar/ejecutivo/suv): ")
    puertas=int(input("Ingrese el número de puertas: "))
    asientos=int(input("Ingrese el número de asientos: "))
    velocidadmaxima=float(input("Ingrese la velocidad máxima en km/h: "))
    color=input("Ingrese el color (blanco/negro/rojo/naranja/amarillo/verde/azul/violeta): ")
    velocidadactual=float(input("Ingrese la velocidad actual en km/h: "))
    esautomatico=input("¿El vehículo es automático? (si/no): ")=="si"
    print()
    return Automovil(marca, modelo, motor, tipodecombustible, tipodeautomovil, puertas, asientos, velocidadmaxima, color, velocidadactual, esautomatico)

p1=datos()
p1.imprimir()
p1.setvelocidadactual(100)
p1.acelerar(20)
p1.desacelerar(50)
p1.frenar()
p1.setvelocidadactual(-20)

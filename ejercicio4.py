from math import pi

class Circulo:
    def __init__(self, radio):
        self.radio=radio

    def calculararea(self):
        return pi*self.radio**2
    
    def calcularperimetro(self):
        return 2*pi*self.radio
        
class Rectangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calculararea(self):
        return self.base*self.altura

    def calcularperimetro(self):
        return 2*self.base+2*self.altura


class Cuadrado:
    def __init__(self, longituddelado):
        self.longituddelado=longituddelado

    def calculararea(self):
        return self.longituddelado**2

    def calcularperimetro(self):
        return 4*self.longituddelado

class Triangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def calculararea(self):
        return self.base*self.altura/2

    def calcularperimetro(self):
        return self.base+self.altura+self.calcularhipotenusa()
    
    def calcularhipotenusa(self):
        return (self.base**2+self.altura**2)**(1/2)

    def saberquetipoes(self):
        if self.base==self.altura==self.calcularhipotenusa():
            return "equilátero"
        elif self.base==self.altura or self.base==self.calcularhipotenusa() or self.altura==self.calcularhipotenusa():
            return "isósceles"
        else:
            return "escaleno"
        
class Rombo:
    def __init__(self, diagonalmayor, diagonalmenor, lado):
        self.diagonalmayor=diagonalmayor
        self.diagonalmenor=diagonalmenor
        self.lado=lado

    def calculararea(self):
        return self.diagonalmayor*self.diagonalmenor/2
    
    def calcularperimetro(self):
        return 4*self.lado

class Trapecio:
    def __init__(self, basemayor, basemenor, altura, lado1, lado2):
        self.basemayor=basemayor
        self.basemenor=basemenor
        self.altura=altura
        self.lado1=lado1
        self.lado2=lado2

    def calculararea(self):
        return (self.basemayor+self.basemenor)*self.altura/2
    
    def calcularperimetro(self):
        return self.basemayor+self.lado1+self.basemenor+self.lado2

def datoscirculo():
    radiodelcirculo=float(input("Ingrese el radio del círculo en centimetros: "))
    print()
    return Circulo(radiodelcirculo)

def datosrectangulo():
    basedelrectangulo=float(input("Ingrese la base del rectángulo en centimetros: "))
    alturadelrectangulo=float(input("Ingrese la altura del rectángulo en centimetros: "))
    print()
    return Rectangulo(basedelrectangulo, alturadelrectangulo)

def datoscuadrado():
    ladodelcuadrado=float(input("Ingrese el lado del cuadrado en centimetros: "))
    print()
    return Cuadrado(ladodelcuadrado)

def datostriangulo():
    basedeltriangulo=float(input("Ingrese la base del triángulo en centimetros: "))
    alturadeltriangulo=float(input("Ingrese la altura del triángulo en centimetros: "))
    print()
    return Triangulo(basedeltriangulo, alturadeltriangulo)

def datosrombo():
    diagonalmayordelrombo=float(input("Ingrese la diagonal mayor del rombo en centimetros: "))
    diagonalmenordelrombo=float(input("Ingrese la diagonal menor del rombo en centimetros: "))
    ladodelrombo=float(input("Ingrese un lado del rombo en centimetros: "))
    print()
    return Rombo(diagonalmayordelrombo, diagonalmenordelrombo, ladodelrombo)

def datostrapecio():
    basemayordeltrapecio=float(input("Ingrese la base mayor del trapecio en centimetros: "))
    basemenordeltrapecio=float(input("Ingrese la base menor del trapecio en centimetros: "))
    alturadeltrapecio=float(input("Ingrese la altura del trapecio en centimetros: "))
    lado1deltrapecio=float(input("Ingrese el lado 1 de trapecio en centimetros: "))
    lado2deltrapecio=float(input("Ingrese el lado 2 del trapecio en centimetros: "))
    print()
    print()
    return Trapecio(basemayordeltrapecio, basemenordeltrapecio, alturadeltrapecio, lado1deltrapecio, lado2deltrapecio)

figura1=datoscirculo()
figura2=datosrectangulo()
figura3=datoscuadrado()
figura4=datostriangulo()
figura5=datosrombo()
figura6=datostrapecio()

def imprimir():
    print(f"El área del círculo es = {figura1.calculararea()}")
    print(f"El perímetro del círculo es = {figura1.calcularperimetro()}")
    print()
    print(f"El área del rectángulo es = {figura2.calculararea()}")
    print(f"El perímetro del rectángulo es = {figura2.calcularperimetro()}")
    print()
    print(f"El área del cuadrado es = {figura3.calculararea()}")
    print(f"El perímetro del cuadrado = {figura3.calcularperimetro()}")
    print()
    print(f"El área del triángulo es = {figura4.calculararea()}")
    print(f"El perímetro del triángulo es = {figura4.calcularperimetro()}")
    print(f"Es un triángulo = {figura4.saberquetipoes()}")
    print()
    print(f"El área del rombo es = {figura5.calculararea()}")
    print(f"El perímetro del rombo es = {figura5.calcularperimetro()}")
    print()
    print(f"El área del trapecio es = {figura6.calculararea()}")
    print(f"El perímetro del trapecio es = {figura6.calcularperimetro()}")

imprimir()

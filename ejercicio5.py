class CuentaBancaria:
    def __init__(self, nombre, apellidos, numerodelacuenta, tipodecuenta, porcentajedeinteresmensual):
        self.nombre=nombre
        self.apellidos=apellidos
        self.numerodelacuenta=numerodelacuenta
        self.tipodecuenta=tipodecuenta
        self.saldo=0
        self.porcentajedeinteresmensual=porcentajedeinteresmensual

    def imprimir(self):
        print(f"Nombre del titular = {self.nombre}")
        print(f"Apellidos del titular = {self.apellidos}")
        print(f"Número de la cuenta = {self.numerodelacuenta}")
        print(f"Tipo de cuenta = {self.tipodecuenta}")
        print(f"Saldo = {self.saldo}")

    def consultarsaldo(self):
        print(f"El saldo actual es: ${self.saldo}")

    def consignar(self, consignacion):
        self.saldo=self.saldo+consignacion
        print(f"Se ha consignado ${consignacion} en la cuenta. El nuevo saldo es ${self.saldo}")

    def retirar(self, retiro):
        if retiro>self.saldo:
            print("No se puede realizar el retiro.")
        else:
            self.saldo=self.saldo-retiro
            print(f"Se ha retirado ${retiro} en la cuenta. El nuevo saldo es ${self.saldo}")

    def aplicarinteres(self):
        valorasumar=self.saldo*self.porcentajedeinteresmensual/100
        self.saldo=self.saldo+valorasumar
        print(f"Se ha consignado ${valorasumar} como resultado de la aplicación de la tasa de interés. El nuevo saldo es: {self.saldo}")

def datos():
    nombre=input("Ingrese el nombre: ")
    apellidos=input("Ingrese los apellidos: ")
    numerodelacuenta=int(input("Ingrese el número de la cuenta: "))
    tipodecuenta=input("Ingrese el tipo de cuenta (ahorros/corriente): ")
    porcentajedeinteresmensual=float(input("Ingrese el porcentaje de interés mensual: "))
    print()
    return CuentaBancaria(nombre, apellidos, numerodelacuenta, tipodecuenta, porcentajedeinteresmensual)

cuenta=datos()
cuenta.imprimir()
cuenta.consignar(200000)
cuenta.consignar(300000)
cuenta.retirar(400000)

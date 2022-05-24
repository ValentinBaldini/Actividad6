class Cuenta:

    def __init__(self, titular, cantidad):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        print("Datos de la cuenta:\nTitular:", self.titular)

    def ingresar(self):
        self.cantidad = int(input("Ingrese dinero: "))
        while self.cantidad<0:
            print("Ingrese un numero positivo")
            self.cantidad = int(input("Ingrese dinero: "))

    def retirar(self):
        retiro = int(input("Cuanto dinero quiere retirar?: "))
        self.cantidad -= retiro

cuenta1 = Cuenta("Valentin Baldini", 0)
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirar()
print("Saldo actualizado: ",cuenta1.cantidad)
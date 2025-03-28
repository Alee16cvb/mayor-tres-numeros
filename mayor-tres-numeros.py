"""
Determina el mayor de tres números ingresados por el teclado
"""
class OrdenandorTresNumeros:
    def __init__(self):
        self.ingresar_numeros()

    def intercambiar_valores(self,numero1, numero2):
        temporal = numero1
        numero1 = numero2
        numero2 = temporal
        return numero1, numero2

    def ingresar_numeros(self):
        self.numero1=int(input("Ingresa el primer numero : "))
        self.numero2=int(input("Ingresa el segundo numero: "))
        self.numero3=int(input("Ingresa el tercer numero : "))

    def ordenar_numeros(self):
        if self.numero1>self.numero2:
           self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)

        if self.numero2>self.numero3:
           self.numero2, self.numero3 = self.intercambiar_valores(self.numero2, self.numero3)

        if self.numero1>self.numero2:
           self.numero1, self.numero2 = self.intercambiar_valores(self.numero1, self.numero2)
    def imprimir_numero(self):
        print(self.numero3)
    def mayor_numero_es(self):
        self.ordenar_numeros()
        return self.numero3

if __name__=="__main__":

    orden = OrdenandorTresNumeros()
    print(f"El numero mayor es: {orden.mayor_numero_es()}")

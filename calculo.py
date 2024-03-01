class Calculo:
    def __init__(self, numero1:int, numero2:int):
        self.numero1 = numero1
        self.numero2 = numero2

    def suma(self):
        self.numero1 + self.numero2
        print("El resultado de la suma es:", self.numero1 + self.numero2)
        
    def resta(self):
        self.numero1 - self.numero2
        print("El resultado de la resta es:", self.numero1 - self.numero2)

    def mult(self):
        self.numero1 * self.numero2
        print("El resultado de la multiplicación es:", self.numero1 * self.numero2)

    def divi(self):
        self.numero1 / self.numero2
        print("El resulto de la división es:", self.numero1 / self.numero2)

if __name__ == "__main__":
    ejemplo = Calculo(5,5)
    ejemplo.suma()
    ejemplo.resta()
    ejemplo.mult()
    ejemplo.divi()

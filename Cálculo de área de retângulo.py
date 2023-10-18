class Retangulo:
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura
    
    def perimetro(self):
        return (self.base + self.altura)*2

# Pedir os valores:
base = (float(input("Insira o valor 'base': ")))
altura = (float(input("Insira o valor 'altura': ")))   

# Criar objeto: 
retangulo1 = Retangulo(base, altura)

# Calculando área e perímetro
area = retangulo1.area()
perimetro = retangulo1.perimetro()

print(area)
print(perimetro)
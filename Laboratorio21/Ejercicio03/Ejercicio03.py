class Figura:
    
    def calcular_area(self):
        pass
    
    def calcular_perimetro(self):
        pass

    def mostrar_datos(self):
        print("Figura genérica")


class Rectangulo(Figura):
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return self.base * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)
    
    def mostrar_datos(self):
        print(
            f"Rectangulo:\n"
            f"Base: {self.base}\n"
            f"Altura: {self.altura}\n"
            f"Area: {self.calcular_area()}\n"
            f"Perimetro: {self.calcular_perimetro()}\n"
        )


class Triangulo(Figura):
    
    def __init__(self, base, altura, lado2, lado3):
        self.base = base
        self.altura = altura
        self.lado2 = lado2
        self.lado3 = lado3
        
    def calcular_area(self):
        return self.base * self.altura * 0.5
    
    def calcular_perimetro(self):
        return self.base + self.lado2 + self.lado3
    
    def mostrar_datos(self):
        print(
            f"Triangulo:\n"
            f"Base: {self.base}\n"
            f"Altura: {self.altura}\n"
            f"Area: {self.calcular_area()}\n"
            f"Perimetro: {self.calcular_perimetro()}\n"
        )


class Circulo(Figura):
    PI = 3.14
    
    def __init__(self, radio):
        self.radio = radio  
        
    def calcular_area(self):
        return self.PI * self.radio ** 2
    
    def calcular_perimetro(self):
        return 2 * self.PI * self.radio
    
    def mostrar_datos(self):
        print(
            f"Circulo:\n"
            f"Radio: {self.radio}\n"
            f"Area: {self.calcular_area()}\n"
            f"Perimetro: {self.calcular_perimetro()}\n"
        )

rectangulo = Rectangulo(10, 5)
triangulo = Triangulo(10, 3, 15, 16)
circulo = Circulo(5)

lista_figuras = [rectangulo, triangulo, circulo]

for figura in lista_figuras:
    figura.mostrar_datos()

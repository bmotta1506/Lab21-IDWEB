import geometria

def ejecutar_programa():
    print("--- Cálculos Geométricos ---")
    
    try:
        r = float(input("Ingresa el radio del círculo: "))
        print(f"Área del círculo: {geometria.area_circulo(r):.2f}")
        b = float(input("Ingresa la base del rectángulo: "))
        a = float(input("Ingresa la altura del rectángulo: "))
        
        print(f"Área: {geometria.area_rectangulo(b, a)}")
        print(f"Perímetro: {geometria.perimetro_rectangulo(b, a)}")
        
    except ValueError:
        print("Error: Por favor ingresa solo números.")

if __name__ == "__main__":
    ejecutar_programa()
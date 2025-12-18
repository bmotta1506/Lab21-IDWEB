class OperadorInvalidoError(Exception):
    """Excepción lanzada cuando el operador no es +, -, * o /."""
    pass

def calcular():
    entrada = input("Introduce la operación (ejemplo: '10 / 2'): ")
    
    try:
        partes = entrada.split()
        
        if len(partes) != 3:
            raise ValueError("Formato incorrecto. Usa: número operador número")
        
        str_num1, operador, str_num2 = partes
        
        num1 = float(str_num1)
        num2 = float(str_num2)
        
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
       
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
                return
            resultado = num1 / num2
        else:
   
            raise OperadorInvalidoError(f"El operador '{operador}' no es válido.")

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: Uno de los valores no es un número válido.")
    except OperadorInvalidoError as e:
        print(f"Error personalizado: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

calcular()
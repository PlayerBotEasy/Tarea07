def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        raise ValueError("No se puede dividir por cero")
    return num1 / num2

try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+ para suma, - para resta, * para multiplicación, / para división): ")

    if operacion == "+":
        resultado = suma(num1, num2)
    elif operacion == "-":
        resultado = resta(num1, num2)
    elif operacion == "*":
        resultado = multiplicacion(num1, num2)
    elif operacion == "/":
        resultado = division(num1, num2)
    else:
        raise ValueError("Operación no válida")

    print("Resultado:", resultado)
except ValueError as e:
    print("Error:", str(e))

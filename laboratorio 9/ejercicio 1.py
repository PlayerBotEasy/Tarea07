def celsius_a_fahrenheit(temperatura):
    return (temperatura * 9/5) + 32

def fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) * 5/9

def convertir_temperatura(temperatura, unidad):
    if unidad.lower() == "c":
        return celsius_a_fahrenheit(temperatura)
    elif unidad.lower() == "f":
        return fahrenheit_a_celsius(temperatura)
    else:
        raise ValueError("Unidad inválida. Por favor, ingrese 'C' para Celsius o 'F' para Fahrenheit.")

try:
    temperatura = float(input("Ingrese la temperatura: "))
    unidad = input("Ingrese la unidad (C para Celsius o F para Fahrenheit): ")
    
    temperatura_convertida = convertir_temperatura(temperatura, unidad)
    
    print("Temperatura convertida:", temperatura_convertida)
except ValueError as e:
    print("Error:", str(e))

def calcular_factorial(numero):
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    return factorial

numero = int(input("Ingrese un número: "))
factorial = calcular_factorial(numero)
print("El factorial de", numero, "es:", factorial)

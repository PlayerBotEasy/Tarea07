numeros = []

for i in range(5):
    numero = float(input("Introduce un número: "))
    numeros.append(numero)

media = sum(numeros) / len(numeros)
print("La media de los números es:", media)

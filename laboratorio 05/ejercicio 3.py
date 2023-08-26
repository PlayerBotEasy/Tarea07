# Listas de números enteros
lista1 = list(range(1, 11))
lista2 = list(range(5, 16))
lista3 = list(range(10, 21))

# a. Convertir las listas en conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)
conjunto3 = set(lista3)

# b. Encontrar el conjunto de números presentes en las tres listas
conjunto_interseccion = conjunto1 & conjunto2 & conjunto3

# c. Encontrar el conjunto de números presentes en al menos una de las listas
conjunto_union = conjunto1 | conjunto2 | conjunto3

# d. Encontrar el conjunto de números presentes en la primera lista pero no en la última
conjunto_diferencia = conjunto1 - conjunto3

# e. Convertir los conjuntos en tuplas y sumar el primer y último elemento de cada tupla
tupla_interseccion = (min(conjunto_interseccion), max(conjunto_interseccion))
tupla_union = (min(conjunto_union), max(conjunto_union))
tupla_diferencia = (min(conjunto_diferencia), max(conjunto_diferencia))

# Sumar el primer y último elemento de cada tupla
suma_tupla_interseccion = sum(tupla_interseccion)
suma_tupla_union = sum(tupla_union)
suma_tupla_diferencia = sum(tupla_diferencia)

print("Conjunto de números en la intersección de las tres listas:", conjunto_interseccion)
print("Conjunto de números en al menos una de las listas:", conjunto_union)
print("Conjunto de números en la primera lista pero no en la última:", conjunto_diferencia)
print("Suma del primer y último elemento de la tupla de intersección:", suma_tupla_interseccion)
print("Suma del primer y último elemento de la tupla de unión:", suma_tupla_union)
print("Suma del primer y último elemento de la tupla de diferencia:", suma_tupla_diferencia)

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# a. Ordenar la lista y encontrar la edad mínima y máxima
edades_ordenadas = sorted(edades)
edad_minima = edades_ordenadas[0]
edad_maxima = edades_ordenadas[-1]

# b. Añadir de nuevo la edad mínima y máxima a la lista
edades.extend([edad_minima, edad_maxima])

# c. Encontrar la edad mediana
n = len(edades)
if n % 2 == 1:
    edad_mediana = edades[n // 2]
else:
    mediana_inf = edades[n // 2 - 1]
    mediana_sup = edades[n // 2]
    edad_mediana = (mediana_inf + mediana_sup) / 2

# d. Encontrar la edad promedio
edad_promedio = sum(edades) / n

# e. Encontrar el rango de las edades
rango_edades = edad_maxima - edad_minima

# f. Comparar el valor de (mínimo - promedio) y (máximo - promedio) usando abs()
diferencia_min_promedio = abs(edad_minima - edad_promedio)
diferencia_max_promedio = abs(edad_maxima - edad_promedio)

# Imprimir los resultados
print("Edades ordenadas:", edades_ordenadas)
print("Edad mínima:", edad_minima)
print("Edad máxima:", edad_maxima)
print("Lista de edades con mínima y máxima añadidas:", edades)
print("Edad mediana:", edad_mediana)
print("Edad promedio:", edad_promedio)
print("Rango de edades:", rango_edades)
print("Diferencia entre mínimo y promedio:", diferencia_min_promedio)
print("Diferencia entre máximo y promedio:", diferencia_max_promedio)

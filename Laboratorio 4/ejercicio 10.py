def es_palindromo(frase):
  """
  Detecta si una frase es un palíndromo.

  Args:
    frase: La frase a evaluar.

  Returns:
    True si la frase es un palíndromo, False de lo contrario.
  """

  # Convertir la frase a minúsculas y eliminar espacios, acentos y signos de puntuación
  frase_limpia = frase.lower().replace(" ", "").replace(",", "").replace(".", "")
  frase_invertida = frase_limpia[::-1]

  # Comparar la frase original con la frase invertida
  return frase_limpia == frase_invertida


# Ejemplo de uso
frase = "Anita lava la tina"

if es_palindromo(frase):
  print("La frase es un palíndromo")
else:
  print("La frase no es un palíndromo")

def cifrar_cesar(mensaje, desplazamiento):
  """
  Cifra un mensaje utilizando el cifrado César.

  Args:
    mensaje: El mensaje a cifrar.
    desplazamiento: El desplazamiento a utilizar.

  Returns:
    El mensaje cifrado.
  """

  # Crear una tabla de cifrado
  alfabeto = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  alfabeto_cifrado = alfabeto[desplazamiento:] + alfabeto[:desplazamiento]

  # Cifrar el mensaje
  mensaje_cifrado = ""
  for letra in mensaje:
    if letra in alfabeto:
      mensaje_cifrado += alfabeto_cifrado[alfabeto.index(letra)]
    else:
      mensaje_cifrado += letra

  return mensaje_cifrado


def descifrar_cesar(mensaje, desplazamiento):
  """
  Descifra un mensaje cifrado utilizando el cifrado César.

  Args:
    mensaje: El mensaje cifrado.
    desplazamiento: El desplazamiento utilizado para cifrar el mensaje.

  Returns:
    El mensaje original.
  """

  return cifrar_cesar(mensaje, -desplazamiento)


# Ejemplo de uso
mensaje = "Hola mundo!"
desplazamiento = 3

mensaje_cifrado = cifrar_cesar(mensaje, desplazamiento)
print("Mensaje cifrado:", mensaje_cifrado)

mensaje_descifrado = descifrar_cesar(mensaje_cifrado, desplazamiento)
print("Mensaje descifrado:", mensaje_descifrado)

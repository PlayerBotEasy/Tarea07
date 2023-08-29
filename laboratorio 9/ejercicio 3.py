import random
import string

def generar_contrasena(longitud):
    try:
        caracteres = string.ascii_letters + string.digits + string.punctuation
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
        return contrasena
    except ValueError as e:
        print("Error:", str(e))

try:
    longitud = int(input("Ingrese la longitud de la contraseña: "))
    contrasena_generada = generar_contrasena(longitud)
    print("Contraseña generada:", contrasena_generada)
except ValueError:
    print("Error: La longitud de la contraseña debe ser un número entero positivo.")

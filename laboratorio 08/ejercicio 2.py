import string
import secrets

def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = []
    
    if longitud < 8:
        print("La longitud de la contraseña debe ser al menos 8 caracteres.")
        return
    
    contrasena.append(secrets.choice(string.ascii_lowercase))
    contrasena.append(secrets.choice(string.ascii_uppercase))
    contrasena.append(secrets.choice(string.digits))
    contrasena.append(secrets.choice(string.punctuation))
    
    for _ in range(longitud - 4):
        contrasena.append(secrets.choice(caracteres))
    
    contrasena_final = ''.join(contrasena)
    return contrasena_final

longitud_deseada = int(input("Ingrese la longitud deseada de la contraseña: "))
contrasena_generada = generar_contrasena(longitud=longitud_deseada)

if contrasena_generada:
    print("Contraseña generada:", contrasena_generada)

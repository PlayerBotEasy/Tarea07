persona = {
    'first_name': 'Edem',
    'last_name': 'Terraza',
    'age': 31,
    'country': 'Peru',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

# a) Comprobar si el diccionario tiene la clave 'skills' y luego imprimir la habilidad del medio
if 'skills' in persona:
    habilidades = persona['skills']
    cantidad_habilidades = len(habilidades)
    if cantidad_habilidades > 0:
        habilidad_media = habilidades[cantidad_habilidades // 2]
        print("Habilidad del medio:", habilidad_media)
    else:
        print("La lista de habilidades está vacía.")

# b) Comprobar si el diccionario tiene la clave 'skills' y luego verificar si tiene la habilidad 'Python'
if 'skills' in persona:
    habilidades = persona['skills']
    if 'Python' in habilidades:
        print("La persona tiene la habilidad 'Python'.")
    else:
        print("La persona no tiene la habilidad 'Python'.")

# c) Comprobar las habilidades de la persona y proporcionar un título según las condiciones
if 'skills' in persona:
    habilidades = persona['skills']
    if habilidades == ['JavaScript', 'React']:
        print("Él es un desarrollador frontend.")
    elif set(habilidades) == {'Node', 'Python', 'MongoDB'}:
        print("Él es un desarrollador backend.")
    elif set(habilidades) == {'React', 'Node', 'MongoDB'}:
        print("Él es un desarrollador fullstack.")
    else:
        print("Título desconocido.")
else:
    print("No se encontraron habilidades en el diccionario de la persona.")

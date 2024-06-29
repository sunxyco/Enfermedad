import csv
import random


def nombres_genesis(num_ciudadanos):
# Lista de nombres y apellidos
    nombres = [
        "Alejandro", "Beatriz", "Carlos", "Diana", "Emilio",
        "Fernanda", "Gabriel", "Hilda", "Ignacio", "Julia",
        "Kevin", "Laura", "Miguel", "Nadia", "Oscar",
        "Patricia", "Ricardo", "Sofía", "Tomás", "Valeria",
        "Walter", "Ximena", "Yolanda", "Zacarías", "Andrés"
    ]

    apellidos = [
        "García", "Martínez", "López", "Hernández", "González",
        "Pérez", "Sánchez", "Ramírez", "Torres", "Flores",
        "Rivera", "Gómez", "Díaz", "Vázquez", "Cruz",
        "Morales", "Ortiz", "Gutiérrez", "Rojas", "Castro",
        "Méndez", "Paredes", "Núñez", "Ramos", "Silva"
    ]

    # Generar 1000 nombres y apellidos aleatorios
    nombres_aleatorios = random.choices(nombres, k=num_ciudadanos)
    apellidos_aleatorios = random.choices(apellidos, k=num_ciudadanos)

    # Crear lista de nombres y apellidos combinados
    nombres_apellidos = list(zip(nombres_aleatorios, apellidos_aleatorios))

    # Escribir los nombres y apellidos en un archivo CSV
    with open("nombres_apellidos.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["nombre", "apellido"])
        writer.writerows(nombres_apellidos)

    print("Archivo CSV generado con éxito.")
    """
    print("hola mundo")
    nombres_genesis()"""
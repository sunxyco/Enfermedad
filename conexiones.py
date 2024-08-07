import numpy as np
import pandas as pd

def mostrar_mostrar_coneciones(self, personas):
	nombres_conexiones = []
	for sujeto in personas:
		nombres_conexiones.append(sujeto.nombre_apellido)

	return nombres_conexiones

def dist_normal(media, des_stand):
	# Inicializa con un valor negativo para entrar al bucle
    numero_aleatorio = -1

    while numero_aleatorio < 0:
    	# Obtén el primer (y único) elemento del array
        numero_aleatorio = np.random.normal(media, des_stand, 1)[0]
    numero_aleatorio_redondeado = round(numero_aleatorio)
    return numero_aleatorio_redondeado

def probabilidad(persona_contagiante, persona_suseptible):

	# conexiones.probabilidad(persona_contagiante, persona_suseptible)
	#-random.random -> genera un numero entre el rango (0.0 , 1.0), se puede usar para comparar las probabilidades
	# Generar un número aleatorio en el rango [0.0, 1.0)
	#random_number = np.random.random()
	#print(random_number)

	if persona_contagiante.familia == persona_suseptible.familia:
		print(f"la persona es un conacto estrecho     prob~ {persona_contagiante.enfermedad.infeccion_probable_familiar}")
		#se usa la probabilidad de infeccion familiar para calcular
		if np.random.random() <= persona_contagiante.enfermedad.infeccion_probable_familiar:
			print("~  estrecho")
			return True
		else:
			print("~ estecho")
			return False
	else:
		print(f"la persona no es un contacto estrecho prob~ {persona_contagiante.enfermedad.infeccion_probable_aleatorio}")
		if np.random.random() <= persona_contagiante.enfermedad.infeccion_probable_aleatorio:
			print("~ no estrecho")
			return True
		else:
			print("~ no estrecho")
			return False

def graficar():
	# Leer el archivo CSV en un DataFrame
	df = pd.read_csv('Data.csv')

	# Mostrar el DataFrame
	print("DataFrame:")
	print(df)

	# Guardar los datos en arreglos separados
	dias = df['Dia'].tolist()
	suseptibles = df['Suseptibles'].tolist()
	infectados = df['Infectados'].tolist()
	personas_sanas = df['Personas Sanas'].tolist()
	recuperados = df['Recuperados'].tolist()

	# Mostrar los arreglos
	print("\nArreglos separados:")
	print("Dias:", dias)
	print("Suseptibles:", suseptibles)
	print("Infectados:", infectados)
	print("Personas Sanas:", personas_sanas)
	print("Recuperados:", recuperados)

	datos_extraidos = [dias, suseptibles, infectados, personas_sanas, recuperados]
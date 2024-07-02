import numpy as np

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
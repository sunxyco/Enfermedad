import numpy as np

#lista

#personas
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#tamaño del subconjunto
tamano_subconjunto = 4


for x in range(10):
	#seleccionar subconjntos aleatorio sin reemplazo
	subconjunto_aleatorio = np.random.choice(lista, size=tamano_subconjunto)

	print("subconjunto aleatorio: ~ ", subconjunto_aleatorio)

	for elemento in subconjunto_aleatorio:
		print(elemento)
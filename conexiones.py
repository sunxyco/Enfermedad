def mostrar_mostrar_coneciones(self, personas):
	nombres_conexiones = []
	for sujeto in personas:
		nombres_conexiones.append(sujeto.nombre_apellido)

	return nombres_conexiones
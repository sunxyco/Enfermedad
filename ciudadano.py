class Ciudadano:
    #ejemplo vincular clases equipo futbol
    self.comunidad = comunidad
    self.id = id
    self.nombre_apellido = nombre_apellido

    #identificador para cada familia
    self.familia = familia

    #referente a la enfermedad en si (la clase)
    self.enfermedad = enfermedad


    #si esta enfermo es tru
    self.estado = False
    #hay dos maneras de enfermarse
    #1 - no conectado (no se ven fisicamente) -> random (baja)

    #2 - conctado (si se ven fisicamente) -> contacto estrecho (entre familia (importanet el id de familia))
    #                                     -> no contacto estrecho (conexion aleatoria entre cada objeto)

    def enfermarse(self):
        self.estado = True

    def recuperarse(self):
        self.estado = False

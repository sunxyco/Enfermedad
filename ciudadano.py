from enfermedad import Enfermedad

class Ciudadano:

    def __init__(self, comunidad, _id, nombre_apellido, familia):
        #ejemplo vincular clases equipo futbol
        self.comunidad = comunidad
        self._id = _id
        self.nombre_apellido = nombre_apellido

        #identificador para cada familia
        self.familia = familia

        #referente a la enfermedad en si (la clase)
        self.enfermedad = None
        #si esta enfermo es tru
        self.estado = False
        #hay dos maneras de enfermarse
        #1 - no conectado (no se ven fisicamente) -> random (baja)

        #2 - conctado (si se ven fisicamente) -> contacto estrecho (entre familia (importanet el id de familia))
        #                                     -> no contacto estrecho (conexion aleatoria entre cada objeto)
        self.inmunidad = False

    def enfermarse(self, enfermedad_clase):
        self.estado = True
        self.enfermedad = enfermedad_clase

    def recuperarse(self):
        self.estado = False
        self.estado = True

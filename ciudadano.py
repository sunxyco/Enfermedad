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

        #2 - conctado (si se ven fisicamente) -> contacto estrecho (entre familia (importanet el id de familia****))
        #                                     -> no contacto estrecho (conexion aleatoria entre cada objeto)
        self.inmunidad = False
        
        """
        ~idea
        self.dias_enfermo = 0
		
		comparar con el atributo ~enfermedad.promedio pasos~ ,
		que se relaciona con le numero de dias que la enfermedad es infeccionsa y tiene la 
		capacidad para infectar a otro ciudadano, si llega a promedio de pasos la persona se recuperara
		"""

        #conexiones que tiene la persona, se puede considerar amikos
        self.conexiones = []

    def enfermarse(self, enfermedad_clase):
        self.estado = True
        self.enfermedad = enfermedad_clase
		#eliminar la realcion cuando se recupere
		
    def recuperarse(self):
        self.estado = False
		#self.enfermedad = None

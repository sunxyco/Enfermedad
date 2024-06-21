from ciudadano import Ciudadano

class Comunidad:
    def __init__(self, num_ciudadanos,
                        promedio_conexion_fisica,
                        enfermedad,
                        num_infectados,
                        probabilidad_conexion_fisica):

        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.num_infectados = num_infectados
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica

        #se crean ciudadanos base, sin comunidad, sin nombre, sin familia (el hombre sin identidad)
        #estos atributos de las personas se incorporaran en otra funcion
        self.ciudadanos = self.crear_ciudadanos(self.num_ciudadanos)

    def crear_ciudadanos(self, num_ciudadanos):
        #arreglo que alergara los obajeto tipo ciudadano
        arreglo_comunidad = []

        #self.ciudadanos.append(ciudadano)
        for x in range(num_ciudadanos):
            print(f"{x} agregar ciudadano")
            x = Ciudadano("comunidad", x, "nombre_apellido", "familia")
            arreglo_comunidad.append(x)
        return arreglo_comunidad

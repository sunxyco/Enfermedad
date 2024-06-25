from ciudadano import Ciudadano
import random

class Comunidad:
    def __init__(self, num_ciudadanos,
                        promedio_conexion_fisica,
                        enfermedad,
                        num_infectados,
                        probabilidad_conexion_fisica,
                        nombre):

        self.num_ciudadanos = num_ciudadanos
        self.promedio_conexion_fisica = promedio_conexion_fisica
        self.enfermedad = enfermedad
        self.num_infectados = num_infectados
        self.probabilidad_conexion_fisica = probabilidad_conexion_fisica
        self.nombre = nombre

        #se crean ciudadanos base, sin comunidad, sin nombre, sin familia (el hombre sin identidad)
        #estos atributos de las personas se incorporaran en otra funcion
        self.ciudadanos = self.crear_ciudadanos(self.num_ciudadanos)

    def numero_integrantes(self, media, desviacion_estandar):
        #la cantidad de integrantes de la familia distribuJen normal con ciertos parametros qe hay q consultar mejor
        #random .gauss retorna un valor random pero en dustribucion normal
        #round redondea 3.7 -> 4 // 3.2 -> 3
        return round(random.gauss(media, desviacion_estandar))


    def crear_ciudadanos(self, num_ciudadanos):
        #arreglo que alergara los obajeto tipo ciudadano
        arreglo_comunidad = []
        """
        id_familia = 0

        media = 3.1
        desviacion_estandar = 1.2

        for i in range(num_personas):
            cantidad_integrantes = numero_integrantes(media, desviacion_estandar)

            for persona in range(cantidad_integrantes):
                persona = Persona(id_persona=i+1, id_familia=id_familia)
                personas.append(persona)

            id_familia += 1 
        return personas"""

        id_familia = 0
        media = 3.1
        desviacion_estandar = 1.2
        id_persona = 1

        #self.ciudadanos.append(ciudadano)
        while id_persona != self.num_ciudadanos + 1:
        #for x in range(num_ciudadanos):
            print(f"{id_persona} agregar ciudadano")

            cantidad_integrantes = self.numero_integrantes(media, desviacion_estandar)
            for persona in range(cantidad_integrantes):
                #se crea la persona /haciendo que la clase se haga referencia hacia si misma (mind blowing cuando cache esto looooooool)
                persona = Ciudadano(self, id_persona, f"nombre_apellido{id_persona}", id_familia)
                arreglo_comunidad.append(persona)
                id_persona += 1
                if id_persona == self.num_ciudadanos + 1:
                    break
            id_familia += 1

        #agregar infectados a la comunidad
        arreglo_comunidad_infectada = self.agregar_infectados_iniciales(num_ciudadanos, self.num_infectados, arreglo_comunidad)

        return arreglo_comunidad_infectada

    def agregar_infectados_iniciales(self, num_ciudadanos, num_infectados, arreglo_comunidad):
        #ranodom sample genera una lista de numeros aleatorios
        numeros_unicos = random.sample(range(num_ciudadanos), num_infectados)
        numeros_unicos.sort()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", numeros_unicos)

        for persona in arreglo_comunidad:
            if persona._id in numeros_unicos:
                print("EUREka~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(persona._id)
                print(persona.nombre_apellido)
                print(persona.estado)
                persona.enfermarse(self.enfermedad)
                print(persona.estado)




        return arreglo_comunidad

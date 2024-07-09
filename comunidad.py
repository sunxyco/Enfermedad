from ciudadano import Ciudadano
import random
import numpy as np
import generador_nombres
import pandas as pd
import conexiones


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
        numero_de_integrantes_de_la_familia = conexiones.dist_normal(media, desviacion_estandar)
        return numero_de_integrantes_de_la_familia


    def crear_ciudadanos(self, num_ciudadanos):
        #arreglo que alergara los obajeto tipo ciudadano
        arreglo_comunidad = []

        id_familia = 0
        media = 3.1
        desviacion_estandar = 1.2
        id_persona = 1

        #se generan los nombres de las personas
        generador_nombres.nombres_genesis(num_ciudadanos)

        #se lee el archivo que se genero recien y se crean los nombres
        df = pd.read_csv("./nombres_apellidos.csv")
        print("creacion de nombres")
        nombres_completos = df["nombre"] + " " + df["apellido"]

        """
        x = 0
        for nombre in nombres_completos:
            print(f"~~~~ {x} ~~~ {nombre}")
            x = x + 1"""

        while id_persona != self.num_ciudadanos + 1:

        #for x in range(num_ciudadanos):
            #print(f"{id_persona} agregar ciudadano")

            cantidad_integrantes = self.numero_integrantes(media, desviacion_estandar)
            for persona in range(cantidad_integrantes):
                #se crea la persona /haciendo que la clase se haga referencia hacia si misma (mind blowing cuando cache esto looooooool)
                
                #se ve acorde a el numero de id-1 la posicion del nombre de la personacd 
                persona = Ciudadano(self, id_persona, nombres_completos[id_persona - 1], id_familia)
                arreglo_comunidad.append(persona)
                id_persona += 1
                if id_persona == self.num_ciudadanos + 1:
                    break
            id_familia += 1

        #agregar infectados a la comunidad

        arreglo_comunidad_con_conexiones = self.generar_conexiones_interpersonas(self.promedio_conexion_fisica, arreglo_comunidad)

        arreglo_comunidad_infectada = self.agregar_infectados_iniciales(num_ciudadanos, self.num_infectados, arreglo_comunidad_con_conexiones)

        return arreglo_comunidad_infectada



    def generar_conexiones_interpersonas(self, promedio_conexion_fisica, arreglo_comunidad):

        #voy a tener que hacer esta funcion toda denuevo xddddd
        #retornara un arreglo con las conexiones ya hechas

        #la cantidad de conexiones que tiene una persona ~dist_Normal, con media promedio_conexion_fisica
        #la cantidad de personas que tendra en persona.conexiones
        for persona_generar_conexiones in arreglo_comunidad:
            cantidad_de_conexiones = conexiones.dist_normal(promedio_conexion_fisica, 1)
            persona_generar_conexiones.conexiones_disponibles = cantidad_de_conexiones

        #con esta funcion se generan las conexiones en tre las personas de la misma familia
        #se le quitara 1a la cantidad de conexiones podibles que puede tener la persona
            for persona_filtrar in arreglo_comunidad:
                if persona_generar_conexiones._id != persona_filtrar._id and persona_generar_conexiones.familia == persona_filtrar.familia:
                    persona_generar_conexiones.conexiones.append(persona_filtrar)
                    persona_generar_conexiones.conexiones_disponibles -= 1

        #se hace este ciclo en un ciclo for aparte porque necesitaos que todos los ciudadanos tengan 
        #definido cuantas conexiones tendran
        for persona_generar_conexiones in arreglo_comunidad:
            #se ve si la perona tiene espacios disponibles para generar conexiones
            if persona_generar_conexiones.conexiones_disponibles != 0:
                while persona_generar_conexiones.conexiones_disponibles != 0:
                    #genera una conexion con un objeto random del arreglo que tambien tiene espacios disponibles

                    arreglo_disponible = []

                    #se genera un arreglo con las personas que tienen conexiones disponibles
                    for persona in arreglo_comunidad:
                        if persona.conexiones_disponibles != 0 and persona._id != persona_generar_conexiones._id:
                            arreglo_disponible.append(persona)

                    if len(arreglo_disponible) == 0:
                        pass

                    #de el arreglo de las personas disponibles se escoge una al azar
                    persona_aleatoria = np.random.choice(arreglo_disponible)

                    if persona_aleatoria in persona_generar_conexiones.conexiones:
                        break
                    else:
                        persona_aleatoria.conexiones.append(persona_generar_conexiones)
                        persona_aleatoria.conexiones_disponibles -= 1

                        persona_generar_conexiones.conexiones.append(persona_aleatoria)
                        persona_generar_conexiones.conexiones_disponibles -= 1

        return arreglo_comunidad


    def agregar_infectados_iniciales(self, num_ciudadanos, num_infectados, arreglo_comunidad):
        #ranodom sample genera una lista de numeros aleatorios que no se repiten
        numeros_unicos = random.sample(range(num_ciudadanos), num_infectados)
        numeros_unicos.sort()
        #print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", numeros_unicos)

        for persona in arreglo_comunidad:
            if persona._id - 1 in numeros_unicos:
                #print("EUREka~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                #print(persona._id)
                #print(persona.nombre_apellido)
                #print(persona.estado)
                persona.enfermarse(self.enfermedad)
                #print(persona.estado)

        return arreglo_comunidad

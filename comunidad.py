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
            print(f"{id_persona} agregar ciudadano")

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
        #personas
        #lista_comunidad = arreglo_comunidad

        #tamaño del subconjunto
        #promedio de conexiones
        tamano_subconjunto = conexiones.dist_normal(promedio_conexion_fisica, 1)

        #a cada persona se le va a asignar un arreglo ~referencia a otros objetos de la misma comunidad, van a ser sus amikos~
        #(me gustaria mostrar las conexiones entre objetos en un grafo)
        for persona in arreglo_comunidad:

            #se filtra la comunidad para quitarle la persona a la que se le estan haciendo las conexiones y las pesonas de su familia
            counidad_filtrada = []

            for persona_filtrar in arreglo_comunidad:
                if persona._id != persona_filtrar._id and persona.familia != persona_filtrar.familia:
                    counidad_filtrada.append(persona_filtrar)


            #seleccionar subconjntos aleatorio sin reemplazo para conexiones al azar
            print(f"~~~~~~ {counidad_filtrada}")
            if len(counidad_filtrada) > 0:
                while tamano_subconjunto > len(counidad_filtrada):
                    tamano_subconjunto -= 1
                subconjunto_aleatorio = np.random.choice(counidad_filtrada, size=tamano_subconjunto, replace=False)
            else:
                subconjunto_aleatorio = []

            #print("conjunto de personas aleatorio: ~ ", subconjunto_aleatorio)
            for elemetno in subconjunto_aleatorio:
                persona.conexiones.append(elemetno)

            #se agrega a la fuerza a las personas que tienen el mismo id de familia
            for persona_comparar in arreglo_comunidad:
                if persona.familia == persona_comparar.familia and persona._id != persona_comparar._id:
                    if persona_comparar not in persona.conexiones:
                        persona.conexiones.append(persona_comparar)


            #print(f"~ conexiones del elemento ~~ {persona.conexiones}")

            """for elemento in subconjunto_aleatorio:
                print(f"~~~~~~~~ {elemento.nombre_apellido}")"""

        return arreglo_comunidad


    def agregar_infectados_iniciales(self, num_ciudadanos, num_infectados, arreglo_comunidad):
        #ranodom sample genera una lista de numeros aleatorios que no se repiten
        numeros_unicos = random.sample(range(num_ciudadanos), num_infectados)
        numeros_unicos.sort()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~", numeros_unicos)

        for persona in arreglo_comunidad:
            if persona._id - 1 in numeros_unicos:
                print("EUREka~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print(persona._id)
                print(persona.nombre_apellido)
                print(persona.estado)
                persona.enfermarse(self.enfermedad)
                #print(persona.estado)

        return arreglo_comunidad

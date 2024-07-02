from comunidad import Comunidad
import conexiones
import random

class Simulador:
    def __init__(self):
        self.__comunidad = None

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad

    def get_comunidad(self ):
        return self.__comunidad

    def run(self, pasos):
        #correr la simulacion
        print("de momento pinta bien")
        print(f"simlador tendra {pasos} pasos")

        print("SIMULADOR ~~~~ ", self.get_comunidad().nombre)

        for iteracion in range(pasos):
            print(f"PASO ~~ {iteracion + 1} \n")

            for persona in self.get_comunidad().ciudadanos:
                print(f"id_{persona._id} {persona.estado} {persona.nombre_apellido} {persona.familia} {conexiones.mostrar_mostrar_coneciones(self, persona.conexiones)}")

            #probando si se pueden infectar -> si se pueden Xd
            """
            test = self.get_comunidad()

            print(test.ciudadanos[0].estado)
            test.ciudadanos[0].enfermarse(test.enfermedad)
            print(test.ciudadanos[0].estado)
            """

            #ciclo para enfermar a la gente
            #se recorre a todos los ciudadanos hasta que se encuentre a alguien que tiene la enfermedad
            arreglo_personas_contagianes = []
            for test in self.get_comunidad().ciudadanos:
                #si tiene la enfermada empieza el proceso aleatorio de enfermar a la demas gente
                if test.estado:
                    #arreglo de personas que pueden contagiar al resto
                    arreglo_personas_contagianes.append(test)
                    print("~~~~~~~~~~~~~~~~funcion de contagiar xd")

            #una ves extraidos las pesronas que tienen la enfermedad es hace la funcnion para que contagien
            #de momento todas las conexiones que tiene la persona se va conttagiar
            for persona_posible_de_contagio in arreglo_personas_contagianes:
                self.contagiar_conexiones(persona_posible_de_contagio)

            presonas_enfermas = 0
            for persona_shi in self.get_comunidad().ciudadanos:
                if persona_shi.estado:
                    presonas_enfermas = presonas_enfermas + 1
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nSe Terminó el dia ~ personas enfermas: {presonas_enfermas} \n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


            print("\n\nDATOS FINAL DEL DIA\n")
            for persona in self.get_comunidad().ciudadanos:
                print(f"id_{persona._id} {persona.estado} {persona.nombre_apellido} {persona.familia} {conexiones.mostrar_mostrar_coneciones(self, persona.conexiones)}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    def contagiar_conexiones(self, persona_contagiante):
        #se va a comparar persona cada una de las personas que tengan conexiones con la persona contagiante
        #si tienen el mismo _id_familiar la probabilidad de contagiarlos sera mayor, si es diferente sera menor

        #mejorar la funcion persona.contagiarse#self.enfermarse
        print("\nDatos ~ persona contagiante ~~~ ", persona_contagiante.nombre_apellido)

        print("posibles contagios  ~~~ ", conexiones.mostrar_mostrar_coneciones(self, persona_contagiante.conexiones))

        conexiones_temporal = persona_contagiante.conexiones
        #ciclo para contagiar a los demas
        
        for persona_suseptible in conexiones_temporal:
            print(f"la persona es un contacto {persona_suseptible._id} ~ {persona_suseptible.nombre_apellido}")

            #solo va a existir un contacto con la probabilidad de self.get_comunidad.probabilidad_conexion_fisica -> 0.8
            if random.random() <= self.get_comunidad().probabilidad_conexion_fisica:
                print("Si hubo contacto")

                #en esta variable se aloja un bool que servira para la funcion de ahora
                probabilidad_de_que_de_enfeme = conexiones.probabilidad(persona_contagiante, persona_suseptible)
                
                #si la persona ya esta enferma ya no se tomara en cuenta
                if persona_suseptible.estado:
                    print(f"Ya esta enfermo ~~ {persona_suseptible.nombre_apellido}")
                #si la persona no esta enferma esta se mandara a la funcion para enfermarse
                else:
                    if probabilidad_de_que_de_enfeme:
                        persona_suseptible.enfermarse(persona_contagiante.enfermedad)
                        print(f"{persona_suseptible.nombre_apellido} ~~~ se ha enfermado")
                        print(f"~ {persona_suseptible.estado} \n")
                    else:
                        print("No es a enfermado")

            else:
                print("No hubo contacto entre las dos personas")

        #persona_contagiante.conexiones = conexiones_temporal
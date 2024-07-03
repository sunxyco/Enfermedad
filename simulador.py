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
        #print("de momento pinta bien")
        print(f"simlador tendra {pasos} pasos")

        print("SIMULADOR ~~~~ ", self.get_comunidad().nombre)

        #Almacenamiento De Datos DE Infectados Por Dia
        adipd = [self.get_comunidad().num_infectados]

        for iteracion in range(pasos):
            print(f"PASO ~~ {iteracion + 1} \n")

            #se muestran las personas la inicio del dia
            for persona in self.get_comunidad().ciudadanos:
                print(f"id_{persona._id} {persona.estado} {persona.nombre_apellido} {persona.familia} {conexiones.mostrar_mostrar_coneciones(self, persona.conexiones)}")

            for persona in self.get_comunidad().ciudadanos:
                if persona.estado:
                    if persona.dias_que_va_a_estar_enfermo == persona.dias_enfermo:
                        persona.recuperarse()
                        print(f"Se ha curado y ha desarrollado inmunidad. {persona.nombre_apellido}")

            #ciclo para enfermar a la gente
            #se recorre a todos los ciudadanos hasta que se encuentre a alguien que tiene la enfermedad
            arreglo_personas_contagianes = []
            for test in self.get_comunidad().ciudadanos:
                #si tiene la enfermada empieza el proceso aleatorio de enfermar a la demas gente
                if test.estado:
                    #arreglo de personas que pueden contagiar al resto
                    arreglo_personas_contagianes.append(test)
                    #print("~~~~~~~~~~~~~~~~funcion de contagiar xd")

            #una ves extraidos las pesronas que tienen la enfermedad es hace la funcnion para que contagien
            #de momento todas las conexiones que tiene la persona se va conttagiar
            for persona_posible_de_contagio in arreglo_personas_contagianes:
                self.contagiar_conexiones(persona_posible_de_contagio)

            #se cuentan las personas enfermas al final del dia
            presonas_enfermas = 0
            for persona_shi in self.get_comunidad().ciudadanos:
                if persona_shi.estado:
                    presonas_enfermas = presonas_enfermas + 1
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\nSe Terminó el dia ~ personas enfermas: {presonas_enfermas} \n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            adipd.append(presonas_enfermas)

            print("\n\nDATOS FINAL DEL DIA\n")
            for persona in self.get_comunidad().ciudadanos:
                if persona.dias_que_va_a_estar_enfermo == None:
                    print(f"id_{persona._id} {persona.estado} d{persona.dias_enfermo}-* f{persona.familia} {persona.nombre_apellido} ~ {conexiones.mostrar_mostrar_coneciones(self, persona.conexiones)}")
                else:
                    print(f"id_{persona._id} {persona.estado} d{persona.dias_enfermo}-{persona.dias_que_va_a_estar_enfermo} f{persona.familia} {persona.nombre_apellido} ~ {conexiones.mostrar_mostrar_coneciones(self, persona.conexiones)}")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"enfermos por dia ~ {adipd}")

    def contagiar_conexiones(self, persona_contagiante):
        #se va a comparar persona cada una de las personas que tengan conexiones con la persona contagiante
        #si tienen el mismo _id_familiar la probabilidad de contagiarlos sera mayor, si es diferente sera menor

        persona_contagiante.dias_enfermo = persona_contagiante.dias_enfermo + 1

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

                if persona_suseptible.inmunidad:
                    print(f"{persona_suseptible.nombre_apellido} Es inmune ~ no se puede enfermear")
                else:
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
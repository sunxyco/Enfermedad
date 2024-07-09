from comunidad import Comunidad
import conexiones
import random
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class Simulador:
    def __init__(self):
        self.__comunidad = None
        self.datos_final_simulacion = []

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad

    def get_comunidad(self ):
        return self.__comunidad

    def run(self, pasos):
        print(f"Simulador tendrá {pasos} pasos")
        print("SIMULADOR ~~~~ ", self.get_comunidad().nombre)

        adipd = np.array([self.get_comunidad().num_infectados])
        adnpo = np.array([0])
        numero_sanos_iniciales = self.get_comunidad().num_ciudadanos - self.get_comunidad().num_infectados
        ads = np.array([numero_sanos_iniciales])
        arreglo_suseptibles = np.array([numero_sanos_iniciales])
        dias = np.array([0])
        datos_totales = ""

        for iteracion in range(pasos):
            print(f"PASO ~~ {iteracion + 1} \n")
            dias = np.append(dias, iteracion + 1)

            contador_inmunes = 0
            c_suseptibles = 0
            presonas_enfermas = 0
            personas_sanas = 0

            for persona_shi in self.get_comunidad().ciudadanos:
                if persona_shi.estado:
                    presonas_enfermas += 1
                else:
                    personas_sanas += 1
            adipd = np.append(adipd, presonas_enfermas)
            ads = np.append(ads, personas_sanas)

            for persona in self.get_comunidad().ciudadanos:
                if persona.inmunidad:
                    contador_inmunes += 1
                if persona.suseptible:
                    c_suseptibles += 1

            adnpo = np.append(adnpo, contador_inmunes)
            arreglo_suseptibles = np.append(arreglo_suseptibles, c_suseptibles)

            datos_dia = f"dia {iteracion + 1}; suseptibles {c_suseptibles}; infectados {presonas_enfermas}; personas sanas {personas_sanas}; recuperados {contador_inmunes}\n"
            datos_totales += datos_dia

            for persona in self.get_comunidad().ciudadanos:
                if persona.estado:
                    if persona.dias_que_va_a_estar_enfermo == persona.dias_enfermo:
                        persona.recuperarse()
                        print(f"Se ha curado y ha desarrollado inmunidad. {persona.nombre_apellido}")

            arreglo_personas_contagianes = []
            for test in self.get_comunidad().ciudadanos:
                if test.estado:
                    arreglo_personas_contagianes.append(test)

            for persona_posible_de_contagio in arreglo_personas_contagianes:
                self.contagiar_conexiones(persona_posible_de_contagio)

        #datos totales se termina imprimieno nomas y no se usa para nada
        print(datos_totales)

        arreglo_datos = np.array([dias, adipd, adnpo, arreglo_suseptibles, ads])

        #se convierte a DataFrame de Pandas
        df = pd.DataFrame(arreglo_datos.T, columns=['dias', 'enfermos por dia', 'recuperados', 'suseptibles', 'sanos'])

        #guardar como CSV
        df.to_csv('datos_simulacion.csv', index=False)

        print(f"Los datos se han almacenado correctamente en 'datos_simulacion.csv'.")


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
    

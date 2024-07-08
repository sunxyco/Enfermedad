from comunidad import Comunidad
import conexiones
import random
import matplotlib.pyplot as plt
import pandas as pd

class Simulador:
    def __init__(self):
        self.__comunidad = None
        self.datos_final_simulacion = []

    def set_comunidad(self, comunidad):
        self.__comunidad = comunidad

    def get_comunidad(self ):
        return self.__comunidad

    def run(self, pasos):
        #correr la simulacion
        #print("de momento pinta bien")
        print(f"simlador tendra {pasos} pasos")

        print("SIMULADOR ~~~~ ", self.get_comunidad().nombre)

        adipd = [self.get_comunidad().num_infectados]
        #Almacenamenito De Datos De Inmunes Por Dia
        adnpo = [0]

        numero_sanos_iniciales = self.get_comunidad().num_ciudadanos - self.get_comunidad().num_infectados
        #Almacenamiento Datos Sanos
        ads = [numero_sanos_iniciales]

        arreglo_suseptibles = [numero_sanos_iniciales]
        datos_totales = ""

        dias = [0]

        for iteracion in range(pasos):
            print(f"PASO ~~ {iteracion + 1} \n")
            dias.append(iteracion + 1)

            contador_inmunes = 0
            c_suseptibles = 0
            #se cuentan las personas enfermas al final del dia
            presonas_enfermas = 0
            personas_sanas = 0

            for persona_shi in self.get_comunidad().ciudadanos:
                if persona_shi.estado:
                    presonas_enfermas = presonas_enfermas + 1
                else:
                    personas_sanas = personas_sanas + 1
            adipd.append(presonas_enfermas)
            ads.append(personas_sanas)            

            for persona in self.get_comunidad().ciudadanos:
                if persona.inmunidad:
                    contador_inmunes = contador_inmunes + 1
                if persona.suseptible:
                    c_suseptibles += 1


            adnpo.append(contador_inmunes)
            arreglo_suseptibles.append(c_suseptibles)

            datos_dia = (f"dia {iteracion + 1}; suseptibles {c_suseptibles}; infectados {presonas_enfermas}; personas sanas {personas_sanas}; recuperados {contador_inmunes}\n")
            datos_totales += datos_dia

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



        print(datos_totales)

        print(f"dias ~ {dias}")
        print(f"enfermos por dia ~ {adipd}")
        print(f"recuperados {adnpo}")
        print(f"suseptibles ~ {arreglo_suseptibles}")
        print(f"sanos ~ {ads}")

        print(len(dias))
        print(len(adipd))
        print(len(adnpo))
        print(len(arreglo_suseptibles))
        print(len(ads))

        arreglo_datos = [dias, adipd, adnpo, arreglo_suseptibles, ads]

        nombre_archivo = "datos_simulacion.txt"

        # Abrir el archivo en modo escritura
        with open(nombre_archivo, 'w') as archivo:
            archivo.write("dias ~ " + str(dias) + "\n")
            archivo.write("enfermos por dia ~ " + str(adipd) + "\n")
            archivo.write("recuperados ~ " + str(adnpo) + "\n")
            archivo.write("suseptibles ~ " + str(arreglo_suseptibles) + "\n")
            archivo.write("sanos ~ " + str(ads) + "\n")

        print(f"Los datos se han almacenado correctamente en '{nombre_archivo}'.")

        """
        for dato in arreglo_datos:
        
        #se guarda la data en un txt
        with open("Data.txt", "w") as archivo:
            archivo.write(datos_totales)
        

        """
        # Convertir los datos totales a un DataFrame de Pandas
        df = pd.DataFrame([x.split('; ') for x in datos_totales.split('\n')], columns=['Dia', 'Suseptibles', 'Infectados', 'Personas Sanas', 'Recuperados'])
        
        # Guardar el DataFrame como archivo CSV
        df.to_csv('Data.csv', index=False)


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
    

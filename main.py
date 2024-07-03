from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador
import pandas as pd

covid = Enfermedad(infeccion_probable_aleatorio=0.2,
                    infeccion_probable_familiar=0.8,
                    #dias que la enfermedad va a existir antes que se cure
                    promedio_pasos=7,
                    nombre="Covis",
                    mortalidad=0.1)

talca = Comunidad(num_ciudadanos=300,
                    #promedios de numero de contactos - puede que haya un numero x de contactos
                    #puede que los contactos sean con una persona infectada o con una persona que esta sana(??????)
                    promedio_conexion_fisica=30,
                    enfermedad = covid,
                    num_infectados=1,
                    probabilidad_conexion_fisica=0.7,
                    nombre = "Talca")

sim = Simulador()
sim.set_comunidad(talca)
sim.run(50)




#numpy      -> resolver ecuaciones diferenciales
#matplotlib -> generar grafico
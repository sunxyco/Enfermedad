from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador
import pandas as pd

covid = Enfermedad(infeccion_probable=0.3,
                    #dias que la enfermedad va a existir antes que se cure
                    promedio_pasos=10,
                    nombre="Covis",
                    mortalidad=0.1)

talca = Comunidad(num_ciudadanos=200,
                    #promedios de numero de contactos - puede que haya un numero x de contactos
                    #puede que los contactos sean con una persona infectada o con una persona que esta sana(??????)
                    promedio_conexion_fisica=9,
                    enfermedad = covid,
                    num_infectados=100,
                    probabilidad_conexion_fisica=0.8,
                    nombre = "Talca")

sim = Simulador()
sim.set_comunidad(talca)
sim.run(45)

#print(sim.get_comunidad().ciudadanos)

#devuelve un arreglo que contiene a todos los ciudadanos
arreglo_ciudadanos = sim.get_comunidad().ciudadanos

#consultar clase persona, ahora mismo los objetos ciudadano estan contenidos en un array que es
#un atributo de comunidad (pensando en relacionar las dos clases de otra menera mmmmmmmmmmmmm)

for persona in arreglo_ciudadanos:
    print("comunidad ~ ", persona.comunidad.nombre)
    print("id        ~ ", persona._id)
    print("nombre    ~ ", persona.nombre_apellido)
    print("familia   ~ ", persona.familia)
    print("estado    ~ ", persona.estado)
    print("Conexiones~ ")

    for amigo in persona.conexiones:
        print(amigo.nombre_apellido)

    try:
        print("enfermedad~ ", persona.enfermedad.nombre)
    except AttributeError:
        print("La persona no tiene una enfermedad asignada.")
    print("          ")

#numpy      -> resolver ecuaciones diferenciales
#matplotlib -> generar grafico
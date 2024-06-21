from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

covid = Enfermedad(infeccion_probable=0.3,
                    promedio_pasos=10)
talca = Comunidad(num_ciudadanos=17,
                    promedio_conexion_fisica=8,
                    enfermedad = covid,
                    num_infectados=10,
                    probabilidad_conexion_fisica=0.8)
sim = Simulador()
sim.set_comunidad(talca)
sim.run(45)

#print(sim.get_comunidad().ciudadanos)

arreglo_ciudadanos = sim.get_comunidad().ciudadanos

#consultar clase persona, ahora mismo los objetos ciudadano estan contenidos en un array que es
#un atributo de comunidad (pensando en relacionar las dos clases de otra menera mmmmmmmmmmmmm)
for persona in arreglo_ciudadanos:
    print(persona._id)
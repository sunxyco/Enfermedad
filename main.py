from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador

covid = Enfermedad(infeccion_probable=0.3,
                    promedio_pasos=10)
talca = Comunidad(num_ciudadanos=20000,
                    promedio_conexion_fisica=8,
                    enfermedad = covid,
                    num_infectados=10,
                    probabilidad_conexion_fisica=0.8)
sim = Simulador()
sim.set_comunidad(talca)
sim.run(45)

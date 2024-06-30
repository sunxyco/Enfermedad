from comunidad import Comunidad
import conexiones

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
            print("PASO ~~ ", iteracion + 1)

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
            for test in self.get_comunidad().ciudadanos:
                #si tiene la enfermada empieza el proceso aleatorio de enfermar a la demas gente
                if test.estado:
                    print("~~~~~~~~~~~~~~~~funcion de contagiar xd")
                    self.contagiar_conexiones(test)

    def contagiar_conexiones(self, persona_contagiante):
        #se va a comparar persona cada una de las personas que tengan conexiones con la persona contagiante
        #si tienen el mismo _id_familiar la probabilidad de contagiarlos sera mayor, si es diferente sera menor

        #mejorar la funcion persona.contagiarse#self.enfermarse
        print("persona contagiante ~~~ ", persona_contagiante.nombre_apellido)

        print("posibles contagios  ~~~ ", conexiones.mostrar_mostrar_coneciones(self, persona_contagiante.conexiones))

        #ciclo para contagiar a los demas
        for persona_suseptible in persona_contagiante.conexiones:
            print(f"la persona es un contacto {persona_suseptible._id} ~ {persona_suseptible.nombre_apellido}")
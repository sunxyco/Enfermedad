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
                print(f"{persona._id} {persona.estado} {persona.nombre_apellido} {persona.familia} {conexiones.mostrar_mostrar_coneciones(self, persona.conexiones)}")
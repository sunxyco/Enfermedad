class Enfermedad:
    def __init__(self, infeccion_probable, promedio_pasos, nombre):
        self.infeccion_probable = infeccion_probable
        self.promedio_pasos = promedio_pasos
        self.nombre = nombre
    """

    # Getters
    def get_infeccion_probable(self):
        return self.__infeccion_probable

    def get_promedio_pasos(self):
        return self.__promedio_pasos

    def get_nombre(self):
        return self.__nombre

    # Setters
    def set_infeccion_probable(self, infeccion_probable):
        self.__infeccion_probable = infeccion_probable

    def set_promedio_pasos(self, promedio_pasos):
        self.__promedio_pasos = promedio_pasos

    def set_nombre(self, nombre):
        self.__nombre = nombre

    """
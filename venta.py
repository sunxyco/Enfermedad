import sys
import gi
gi.require_version('Gtk', '4.0')
# from os import remove
from gi.repository import Gtk
from enfermedad import Enfermedad
from comunidad import Comunidad
from simulador import Simulador
import pandas as pd
import conexiones
import matplotlib.pyplot as plt


def on_quit_action(self, _action):
    quit()

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Box principal
        self.main_box = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        self.set_child(self.main_box)

        # Menu
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("Simulador Enfemredad")
        box_izquierda = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)

        box_enfermedad = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        box_comunidad = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        box_simulador = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)

        label_informacion = Gtk.Label()
        label_informacion.set_text("~ ⚠Informacion Ingreso de Datos⚠ ~\nProb -> (0.0 - 1.0) / Prom -> Int(1,2,3,...)\n")
        self.main_box.append(label_informacion)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_enfermedad1 = Gtk.Label()
        label_enfermedad1.set_text("~~Parametros Enfermedad~~")

        label_enfermedad2 = Gtk.Label()
        label_enfermedad2.set_text("Prob. Infeccion - aleatorio")
        self.entry1_enfermedad = Gtk.Entry()
        label_enfermedad3 = Gtk.Label()
        label_enfermedad3.set_text("Prob. Infeccion - Familiar")
        self.entry2_enfermedad = Gtk.Entry()
        label_enfermedad4 = Gtk.Label()
        label_enfermedad4.set_text("Prom. Pasos")
        self.entry3_enfermedad = Gtk.Entry()
        label_enfermedad5 = Gtk.Label()
        label_enfermedad5.set_text("Nombre")
        self.entry4_enfermedad = Gtk.Entry()

        self.entry1_enfermedad.set_placeholder_text("~ def_0.1")
        self.entry2_enfermedad.set_placeholder_text("~ def_0.4")
        self.entry3_enfermedad.set_placeholder_text("~ def_6")
        self.entry4_enfermedad.set_placeholder_text("Covidd")

        box_enfermedad.append(label_enfermedad1)
        box_enfermedad.append(label_enfermedad5)
        box_enfermedad.append(self.entry4_enfermedad)
        box_enfermedad.append(label_enfermedad2)
        box_enfermedad.append(self.entry1_enfermedad)
        box_enfermedad.append(label_enfermedad3)
        box_enfermedad.append(self.entry2_enfermedad)
        box_enfermedad.append(label_enfermedad4)
        box_enfermedad.append(self.entry3_enfermedad)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_comunidad = Gtk.Label()
        label_comunidad.set_text("~~Parametros comunidad~~")

        self.entry1_comunidad = Gtk.Entry()
        self.entry2_comunidad = Gtk.Entry()
        self.entry3_comunidad = Gtk.Entry()
        self.entry4_comunidad = Gtk.Entry()
        self.entry5_comunidad = Gtk.Entry()

        label_comunidad1 = Gtk.Label()
        label_comunidad1.set_text("N° Ciudadanos")
        label_comunidad2 = Gtk.Label()
        label_comunidad2.set_text("Nombre")
        label_comunidad3 = Gtk.Label()
        label_comunidad3.set_text("Prom. Conexion fisica")
        label_comunidad5 = Gtk.Label()
        label_comunidad5.set_text("N° Infectaods iniciales")
        label_comunidad4 = Gtk.Label()
        label_comunidad4.set_text("Prob. Conexion Fisica")


        self.entry1_comunidad.set_placeholder_text("Def_800")
        self.entry5_comunidad.set_placeholder_text("Talca")
        self.entry2_comunidad.set_placeholder_text("Def_6")
        self.entry3_comunidad.set_placeholder_text("Def_1")
        self.entry4_comunidad.set_placeholder_text("Def_0.6")

        box_comunidad.append(label_comunidad)
        box_comunidad.append(label_comunidad2)
        box_comunidad.append(self.entry5_comunidad)
        box_comunidad.append(label_comunidad1)
        box_comunidad.append(self.entry1_comunidad)
        box_comunidad.append(label_comunidad3)
        box_comunidad.append(self.entry2_comunidad)
        box_comunidad.append(label_comunidad5)
        box_comunidad.append(self.entry3_comunidad)
        box_comunidad.append(label_comunidad4)
        box_comunidad.append(self.entry4_comunidad)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_simulador = Gtk.Label()
        label_simulador.set_text("~~Parametros simulador~~")

        self.entry1_simulador = Gtk.Entry()
        label_enfermedad4 = Gtk.Label()
        label_enfermedad4.set_text("N° Pasos")

        self.entry1_simulador.set_placeholder_text("Dias a simular def_60")

        box_simulador.append(label_simulador)
        box_simulador.append(self.entry1_simulador)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        box_izquierda.append(box_enfermedad)
        box_izquierda.append(box_comunidad)
        box_izquierda.append(box_simulador)


        boton = Gtk.Button()
        boton.set_label("Simular")
        boton.connect("clicked", self.clic_simular)

        self.main_box.append(box_izquierda)
        self.main_box.append(boton)


    def clic_simular(self, widget):

        try:
            infeccion_probable_aleatorio = float(self.entry1_enfermedad.get_text())
        except ValueError:
            infeccion_probable_aleatorio = 0.1
        
        try:
            infeccion_probable_familiar = float(self.entry2_enfermedad.get_text())
        except ValueError:
            infeccion_probable_familiar = 0.4
            # Manejar el error aquí
       
        try:
            promedio_pasos = int(self.entry3_enfermedad.get_text())
        except ValueError:
            promedio_pasos = 6
            # Manejar el error aquí

        covid = Enfermedad(infeccion_probable_aleatorio = infeccion_probable_aleatorio,
                            infeccion_probable_familiar = infeccion_probable_familiar,
                            #fias que antes de ser inmune
                            promedio_pasos = promedio_pasos,
                            nombre = self.entry4_enfermedad.get_text())

        try:
            num_ciudadanos = int(self.entry1_comunidad.get_text())
        except ValueError:
            num_ciudadanos = 800
        
        try:
            promedio_conexion_fisica = int(self.entry2_comunidad.get_text())
        except ValueError:
            promedio_conexion_fisica = 6
        
        try:
            num_infectados = int(self.entry3_comunidad.get_text())
        except ValueError:
            num_infectados = 1
        
        try:
            probabilidad_conexion_fisica = float(self.entry4_comunidad.get_text())
        except ValueError:
            probabilidad_conexion_fisica = 0.6

        talca = Comunidad(num_ciudadanos=num_ciudadanos,
                            promedio_conexion_fisica=promedio_conexion_fisica,
                            enfermedad = covid,
                            num_infectados=num_infectados,
                            probabilidad_conexion_fisica=probabilidad_conexion_fisica,
                            nombre = self.entry5_comunidad.get_text())

        sim = Simulador()
        sim.set_comunidad(talca)

        try:
            dias_simular = int(self.entry1_simulador.get_text())
        except ValueError:
            dias_simular = 60

        sim.run(dias_simular)

        #hace todo el algoritmo para hacer la simulaicon y guardar los datos en un .txt
        #y despues cierra toda la aplicacion porque en mi caso
        #tuve una incompatibilidad entre gtk y mathplotlib
        #entonces cuando se ejecuta la simulacion se guardan los datos, se cierra la aplicacion
        #y se leen los datos para ponerlos en un grafico
        self.destroy()

class MyApp(Gtk.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def do_activate(self):
        active_window = self.props.active_window
        if active_window:
            active_window.present()
        else:
            self.win = MainWindow(application=self)
            self.win.present()

app = MyApp()
app.run(sys.argv)

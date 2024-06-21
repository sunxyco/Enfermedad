import sys
import gi
gi.require_version('Gtk', '4.0')
# from os import remove
from gi.repository import Gio, GObject, Gtk, Gdk, GdkPixbuf, GLib
from rdkit.Chem import MolFromMolFile
from rdkit.Chem.Draw import MolToImage
from rdkit.Chem import MolFromMolFile, FindMolChiralCenters
from gi.repository import Gtk


def on_quit_action(self, _action):
    quit()

class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Box principal
        self.main_box = Gtk.Box.new(Gtk.Orientation.HORIZONTAL, 6)
        self.set_child(self.main_box)

        # Menu
        header_bar = Gtk.HeaderBar.new()
        self.set_titlebar(titlebar=header_bar)
        self.set_title("prueba")
        box_izquierda = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        box_derecha = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)

        box_enfermedad = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        box_comunidad = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)
        box_simulador = Gtk.Box.new(Gtk.Orientation.VERTICAL, 6)

        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_enfermedad = Gtk.Label()
        label_enfermedad.set_text("Parametros Enfermedad")

        entry1_enfermedad = Gtk.Entry()
        entry2_enfermedad = Gtk.Entry()
        #entry3_enfermedad = Gtk.EnGtk.Entry()

        entry1_enfermedad.set_placeholder_text("Prob. Infeccion")
        entry2_enfermedad.set_placeholder_text("Prom. Pasos")

        box_enfermedad.append(label_enfermedad)
        box_enfermedad.append(entry1_enfermedad)
        box_enfermedad.append(entry2_enfermedad)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_comunidad = Gtk.Label()
        label_comunidad.set_text("Parametros comunidad")

        entry1_comunidad = Gtk.Entry()
        entry2_comunidad = Gtk.Entry()
        entry3_comunidad = Gtk.Entry()
        entry4_comunidad = Gtk.Entry()
        #entry3_comunidad = Gtk.EnGtk.Entry()

        entry1_comunidad.set_placeholder_text("N° Ciudadanos")
        entry2_comunidad.set_placeholder_text("Prom. Conexion fisica")
        entry3_comunidad.set_placeholder_text("N° Infectados iniciales")
        entry4_comunidad.set_placeholder_text("Prob Conexion fisica")

        box_comunidad.append(label_comunidad)
        box_comunidad.append(entry1_comunidad)
        box_comunidad.append(entry2_comunidad)
        box_comunidad.append(entry3_comunidad)
        box_comunidad.append(entry4_comunidad)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        label_simulador = Gtk.Label()
        label_simulador.set_text("Parametros simulador")

        entry1_simulador = Gtk.Entry()

        entry1_simulador.set_placeholder_text("N° Pasos")

        box_simulador.append(label_simulador)
        box_simulador.append(entry1_simulador)
        #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        box_izquierda.append(box_enfermedad)
        box_izquierda.append(box_comunidad)
        box_izquierda.append(box_simulador)

        #Image Gtk.? Image or Picture
        imagen = Gtk.Picture()
        imagen = Gtk.Image.new()
        imagen.set_pixel_size(300)

        label = Gtk.Label()
        label.set_text("Graficar")

        box_derecha.append(label)
        box_derecha.append(imagen)

        self.main_box.append(box_izquierda)
        self.main_box.append(box_derecha)



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

import venta
import graficar

print("Hola Mundo")

#aki llamo a la funcion x ~ nose porque se abre la ventana,
#pero era justo lo que queria hacer xd

dias, enfermos, recuperados, suseptibles, sanos = graficar.leer_datos_simulacion()

graficar.graficar_simulacion(dias, enfermos, recuperados, suseptibles, sanos)
#graficar.generar_graficar()
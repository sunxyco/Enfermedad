import matplotlib.pyplot as plt

# Abre un archivo en modo lectura ('r' indica lectura, que es el modo por defecto)
# Abre el archivo en modo lectura
with open('datos_simulacion.txt', 'r') as archivo:
    contenido = archivo.read()

# Divide el contenido en líneas (asumiendo que solo hay una línea)
linea = contenido.strip()

# Encuentra las posiciones de los corchetes
inicio_dias = linea.find('[')
fin_dias = linea.find(']')
inicio_enfermos = linea.find('[', fin_dias)
fin_enfermos = linea.find(']', inicio_enfermos)
inicio_recuperados = linea.find('[', fin_enfermos)
fin_recuperados = linea.find(']', inicio_recuperados)
inicio_suseptibles = linea.find('[', fin_recuperados)
fin_suseptibles = linea.find(']', inicio_suseptibles)
inicio_sanos = linea.find('[', fin_suseptibles)
fin_sanos = linea.find(']', inicio_sanos)

# Extrae y convierte los datos en listas
dias = list(map(int, linea[inicio_dias+1:fin_dias].split(', ')))
enfermos = list(map(int, linea[inicio_enfermos+1:fin_enfermos].split(', ')))
recuperados = list(map(int, linea[inicio_recuperados+1:fin_recuperados].split(', ')))
suseptibles = list(map(int, linea[inicio_suseptibles+1:fin_suseptibles].split(', ')))
sanos = list(map(int, linea[inicio_sanos+1:fin_sanos].split(', ')))

# Imprime los datos para verificar
print("Datos extraidos exitosamente")
print("Días:", dias)
print("Enfermos por día:", enfermos)
print("Recuperados:", recuperados)
print("Suseptibles:", suseptibles)
print("Sanos:", sanos)


# Graficar los datos
plt.plot(dias, enfermos, label='Enfermos')
plt.plot(dias, recuperados, label='Recuperados')
plt.plot(dias, suseptibles, label='Suseptibles')
plt.plot(dias, sanos, label='Sanos')

# Personalizar el gráfico
plt.xlabel('Días')
plt.ylabel('Cantidad')
plt.title('Evolución de la enfermedad')
plt.legend()  # Mostrar leyenda

# Mostrar el gráfico
plt.grid(True)  # Activar la cuadrícula
plt.tight_layout()  # Ajustar el diseño
plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def leer_datos_simulacion():
    # Cargar el archivo CSV
    df = pd.read_csv('datos_simulacion.csv')

    #se extraen los datos de cada columna y se almacenan en arrays que luego se graficaran
    dias = np.array(df['dias'])
    enfermos = np.array(df['enfermos por dia'])
    recuperados = np.array(df['recuperados'])
    suseptibles = np.array(df['suseptibles'])
    sanos = np.array(df['sanos'])


    return dias, enfermos, recuperados, suseptibles, sanos

def graficar_simulacion(dias, enfermos, recuperados, suseptibles, sanos):
    # Graficar los arrays

    plt.plot(dias, enfermos, label='Enfermos')
    plt.plot(dias, recuperados, label='Recuperados')
    plt.plot(dias, suseptibles, label='Suseptibles')
    plt.plot(dias, sanos, label='Sanos')

    # Personalizar el gráfico
    plt.xlabel('Días')
    plt.ylabel('Cantidad de personas')
    plt.title('Evolución de la enfermedad')
    plt.legend()  # Mostrar leyenda
    plt.grid(True)  # Activar la cuadrícula

    # Guardar la gráfica como imagen PNG
    plt.savefig('evolucion_enfermedad.png')

    # Mostrar la gráfica
    plt.show()
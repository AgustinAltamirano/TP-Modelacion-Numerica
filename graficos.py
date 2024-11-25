import math
import time
import matplotlib.pyplot as plt
import numpy as np
from operaciones import gauss_seidel_sin_amortiguamiento, estimar_orden_de_convergencia, resolver
from funciones_auxiliares import funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante, funcion_de_terreno_con_loma_de_burro, derivada_de_funcion_de_terreno_con_loma_de_burro

def graficar_orden_de_convergencia(betas, paso, funcion_de_terreno, derivada_de_funcion_de_terreno):
    ordenes_de_convergencia = []

    for b in betas:
        orden = estimar_orden_de_convergencia(paso, b, funcion_de_terreno, derivada_de_funcion_de_terreno)
        ordenes_de_convergencia.append(orden)

    plt.figure(figsize=(10, 6))
    plt.plot(betas, ordenes_de_convergencia, marker='o')
    plt.title('Orden de convergencia para diferentes valores de beta')
    plt.xlabel('Beta')
    plt.ylabel('Orden de convergencia')
    plt.grid(True)
    plt.show()

def graficar_valores_y(betas, paso, funcion_de_terreno, derivada_de_funcion_de_terreno):
    plt.figure(figsize=(10, 6))

    for b in betas:
        _, y_values = resolver(paso, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
        t_values = [i * paso for i in range(len(y_values))]
        plt.plot(t_values, y_values, label=f'b = {b}')

    plt.title('Comparación de valores de y con diferentes valores de beta')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Valor de y')
    plt.legend()
    plt.grid(True)
    plt.show()

def comparar_valores_y(paso, b):

    _, y_values_constante = resolver(paso, b, False, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)
    _, y_values_burro = resolver(paso, b, False, funcion_de_terreno_con_loma_de_burro, derivada_de_funcion_de_terreno_con_loma_de_burro)

    t_values = [i * paso for i in range(len(y_values_constante))]

    plt.figure(figsize=(10, 6))
    plt.plot(t_values, y_values_constante, label='Terreno Constante')
    plt.plot(t_values, y_values_burro, label='Loma de Burro')
    plt.title('Comparación de valores de y entre terreno constante y loma de burro')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Valor de y')
    plt.legend()
    plt.grid(True)
    plt.show()


def comparar_valores_de_carroceria_con_terreno(paso, b):

    valores_terreno = [funcion_de_terreno_con_loma_de_burro(i) for i in np.arange(0, 5, paso)]
    _, y_values_burro = resolver(paso, b, False, funcion_de_terreno_con_loma_de_burro, derivada_de_funcion_de_terreno_con_loma_de_burro)
    diferencia = [y_values_burro[i] - valores_terreno[i] for i in range(len(valores_terreno))]

    t_values = [i * paso for i in range(len(valores_terreno))]

    plt.figure(figsize=(10, 6))
    plt.plot(t_values, valores_terreno, label='Terreno con loma de burro')
    plt.plot(t_values, y_values_burro, label='Carrocería')
    plt.plot(t_values, diferencia, label='Diferencia entre ambos')
    plt.title('Comparación de valores de y de la carrocería con el terreno')
    plt.xlabel('Tiempo (s)')
    plt.ylabel('Valor de y')
    plt.legend()
    plt.grid(True)
    _, y_max = plt.ylim()
    plt.yticks(np.arange(-0.10, y_max, 0.01))

    plt.show()

def comparar_tiempos(betas, paso, funcion_de_terreno, derivada_de_funcion_de_terreno):
    tiempos = []

    for b in betas:
        start_time = time.time()
        resolver(paso, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
        end_time = time.time()
        tiempos.append(end_time - start_time)

    plt.figure(figsize=(10, 6))
    plt.plot(betas, tiempos)
    plt.title('Tiempo de ejecución para diferentes valores de beta')
    plt.xlabel('Beta')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.grid(True)
    plt.show()
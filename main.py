import math
import time
import matplotlib.pyplot as plt
import numpy as np
from operaciones import gauss_seidel_sin_amortiguamiento, estimar_orden_de_convergencia
from graficos import graficar_orden_de_convergencia, graficar_valores_y, comparar_tiempos, comparar_valores_y, comparar_valores_de_carroceria_con_terreno
from funciones_auxiliares import funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante, funcion_de_terreno_con_loma_de_burro, derivada_de_funcion_de_terreno_con_loma_de_burro

def main():
    paso = 0.005
    betas = [0, 0.25, 0.5, 0.75, 1]
    # generar 500 betas entre 0 y 1
    #betas = np.linspace(0, 1, 500)

    # Graficar el orden de convergencia para una serie de betas dadas dependiendo de si es constante o loma de burro
    #graficar_orden_de_convergencia(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    #Graficar los valores de y para una serie de betas dados, dependiendo tambien de si es constante o loma de burro
    #graficar_valores_y(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    # Comparar tiempos para conseguir beta de una serie de betas dadas, la funcion se le pasa como parametro
    # comparar_tiempos(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    # Comparar valores de y entre terreno constante y loma de burro con beta = 0.5
    # comparar_valores_y(paso, 0.5)

    # Comparar valores de carroceria con terreno
    comparar_valores_de_carroceria_con_terreno(paso, 0.5)

if __name__ == "__main__":
    main()
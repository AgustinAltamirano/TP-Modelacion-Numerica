from sys import argv
import math
import time
import matplotlib.pyplot as plt
import numpy as np
from operaciones import gauss_seidel_sin_amortiguamiento, estimar_orden_de_convergencia
from graficos import graficar_orden_de_convergencia, graficar_valores_y, comparar_tiempos, comparar_valores_y, comparar_valores_de_carroceria_con_terreno
from funciones_auxiliares import funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante, funcion_de_terreno_con_loma_de_burro, derivada_de_funcion_de_terreno_con_loma_de_burro


def main(paso, betas):
    # Genera una cantidad bcant de betas entre bmin y bmax

    print("Analisis de respuesta del método para el siguiente conjunto de valores:")
    print("Paso seleccionado: " + str(paso))
    print("Betas a evaluar: " + str(betas))

    # Graficar el orden de convergencia para una serie de betas dadas dependiendo de si es constante o loma de burro
    ordenes_conv = graficar_orden_de_convergencia(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    # Graficar los valores de y para una serie de betas dados, dependiendo tambien de si es constante o loma de burro
    puntos_por_b = graficar_valores_y(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    # Comparar tiempos para conseguir beta de una serie de betas dadas, la funcion se le pasa como parametro
    tiempos = comparar_tiempos(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    output = open("output.txt", "w")

    output.write("Paso: " + str(paso) + "\n")
    output.write("\n")

    output.write("Orden por tiempo de ejecución: \n")
    t_inv = [(v,k) for k,v in tiempos.items()]
    t_inv.sort()

    output.write("(mejor)\n")

    for v, k in t_inv:
        output.write("Beta = " + str(k) + "; Tiempo = " + str(v) + "\n")

    output.write("(peor)\n\n")

    for b in betas:
        output.write("-- Beta = " + str(b) + " --\n")
        output.write("Orden de convergencia: " + str(ordenes_conv[b]) + "\n")
        output.write("\n")

        val_t, val_y = puntos_por_b[b]

        for dt, y in zip(val_t, val_y):
            output.write("dt = " + str(dt) + "; y = " + str(y) + "\n")

        output.write("\n")

        output.write("Tiempo de ejecución: " + str(tiempos[b]) + "\n")
        output.write("\n")

    output.close()


def main2():
    pass
    # Comparar valores de y entre terreno constante y loma de burro con beta = 0.5
    # comparar_valores_y(paso, 0.5)

    # Comparar valores de carroceria con terreno
    # comparar_valores_de_carroceria_con_terreno(paso, 0.5)


if __name__ == "__main__":
    # python3 main.py <paso> <betas>
    # ej: python3 main.py 0.005 0,0.25,0.5,0.75,1
    if len(argv) == 3:
        main(float(argv[1]), list(map(lambda a: float(a), argv[2].split(','))))
    else:
        print("Numero de argumentos incorrecto")
        exit(1)


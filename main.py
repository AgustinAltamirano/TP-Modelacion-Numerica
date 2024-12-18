from sys import argv
from operaciones import setLambda, setK, getK, getLambda
from graficos import graficar_orden_de_convergencia, graficar_valores_y, comparar_tiempos, comparar_valores_y, \
    comparar_valores_de_carroceria_con_terreno
from funciones_auxiliares import funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante


def main(paso, betas):
    print("Analisis de respuesta del método para el siguiente conjunto de valores:")
    print("Paso seleccionado: " + str(paso))
    print("Betas a evaluar: " + str(betas))

    # Graficar el orden de convergencia para una serie de betas dadas dependiendo de si es constante o loma de burro
    ordenes_conv = graficar_orden_de_convergencia(betas, paso, funcion_de_terreno_constante,
                                                  derivada_de_funcion_de_terreno_constante)

    # Graficar los valores de y para una serie de betas dados, dependiendo tambien de si es constante o loma de burro
    puntos_por_b = graficar_valores_y(betas, paso, funcion_de_terreno_constante,
                                      derivada_de_funcion_de_terreno_constante)

    # Comparar tiempos para conseguir beta de una serie de betas dadas, la funcion se le pasa como parametro
    tiempos = comparar_tiempos(betas, paso, funcion_de_terreno_constante, derivada_de_funcion_de_terreno_constante)

    for b in betas:
        print(f"Resultado final para beta = {b}: y = {puntos_por_b[b][1][-1]}")

    output = open("output.txt", "w")

    output.write("K: " + str(getK()) + "\n")
    output.write("Lambda: " + str(getLambda()) + "\n")
    output.write("Paso: " + str(paso) + "\n")
    output.write("\n")

    output.write("Orden por tiempo de ejecución: \n")
    t_inv = [(v, k) for k, v in tiempos.items()]
    t_inv.sort()

    output.write("(mejor)\n")

    for v, k in t_inv:
        output.write("Beta = " + str(k) + "; Tiempo = " + str(v) + "\n")

    output.write("(peor)\n\n")

    output.write("Orden por convergencia: \n")
    o_inv = [(v, k) for k, v in ordenes_conv.items()]
    o_inv.sort(reverse=True)

    output.write("(mejor)\n")

    for v, k in o_inv:
        output.write("Beta = " + str(k) + "; Orden de conv. = " + str(v) + "\n")

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


def main2(paso, beta):
    # Comparar valores de y entre terreno constante y loma de burro con beta
    y_final = comparar_valores_y(paso, beta)

    print(f"Resultado final para beta = {beta}: y = {y_final}")

    # Comparar valores de carroceria con terreno
    comparar_valores_de_carroceria_con_terreno(paso, beta)


if __name__ == "__main__":
    # ejercicio 1
    # python3 main.py 1 <val k> <val lambda> <paso> <betas>
    # ej1: python3 main.py 1 25000 0 0.005 0,0.25,0.5,0.75,1

    # ejercicio 2
    # python3 main.py 2 <val k> <val lambda> <paso> <beta>
    # ej2: python3 main.py 2 25000 750 0.005 0.5
    if len(argv) == 6:
        _, ej, val_k, val_l, paso, betas = argv

        setLambda(val_l)
        setK(val_k)

        if argv[1] == "1":
            main(float(paso), list(map(lambda a: float(a), betas.split(','))))
        elif argv[1] == "2":
            main2(float(paso), float(betas))
        else:
            print("Parametros invalidos")
            exit(1)
    else:
        print("Numero de argumentos incorrecto")
        exit(1)

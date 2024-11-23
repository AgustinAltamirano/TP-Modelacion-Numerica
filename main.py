import math
import time
import matplotlib.pyplot as plt

MASA = 110691 / 200
CONSTANTE_ELASTICA = 25000
CONSTANTE_AMORTIGUAMIENTO = 0
Y_INICIAL = 0
Z_INICIAL = 0
TIEMPO_FINAL = 5

def funcion_de_terreno_constante(t):
    return 0.1

def derivada_de_funcion_de_terreno_constante(t):
    return 0

def funcion_de_terreno_con_loma_de_burro(t):
    if (t <= 1):
        return 0

    if (t > 1 and t <= 1.2):
        return 0.5 * t - 0.5
    
    if (t > 1.2 and t <= 1.4):
        return 0.1
    
    if (t > 1.4 and t <= 1.6):
        return -0.5 * t + 0.8
    
    return 0

def derivada_de_funcion_de_terreno_con_loma_de_burro(t):
    if (t > 1 and t <= 1.2):
        return 0.5
    
    if (t > 1.4 and t <= 1.6):
        return -0.5
    
    return 0


def gauss_seidel_sin_amortiguamiento(t_actual, y_actual, z_actual, paso, b, funcion_de_terreno, derivada_de_funcion_de_terreno):
    c_actual = funcion_de_terreno(t_actual)
    c_siguiente = funcion_de_terreno(t_actual + paso)
    semilla_y, semilla_z = siguiente_valor_de_euler_explicito_sin_amortiguamiento(c_actual, y_actual, z_actual, paso)
    y_siguiente = semilla_y
    z_siguiente = semilla_z
    c_siguiente_derivada = derivada_de_funcion_de_terreno(t_actual + paso)
    c_actual_derivada = derivada_de_funcion_de_terreno(t_actual)

    for _ in range(25):
        y_siguiente = y_actual + paso * ((1 - b) * z_actual + b * z_siguiente)
        z_siguiente = (1 / (1 + paso * b * CONSTANTE_AMORTIGUAMIENTO / MASA)) * (z_actual + (paso/MASA) *(b * (CONSTANTE_ELASTICA * (c_siguiente - y_siguiente) + CONSTANTE_AMORTIGUAMIENTO*c_siguiente_derivada) + (1 - b) * CONSTANTE_ELASTICA * (c_actual - y_actual) + CONSTANTE_AMORTIGUAMIENTO*(c_actual_derivada - z_actual)))

    return y_siguiente, z_siguiente

def siguiente_valor_de_euler_explicito_sin_amortiguamiento(c, y_n, z_n, paso):
    y_siguiente = y_n + paso * z_n
    z_siguiente = z_n + paso * CONSTANTE_ELASTICA / MASA * (c - y_n)
    return y_siguiente, z_siguiente


def resolver(paso, b, imprimir_valores_intermedios, funcion_de_terreno, derivada_de_funcion_de_terreno):
    y_actual = Y_INICIAL 
    z_actual = Z_INICIAL

    if imprimir_valores_intermedios:
        print(f"Avance número {0}, t = {0}, y = {y_actual}")

    for avance_actual in range(1, int(TIEMPO_FINAL/paso) + 1):
        t_actual = avance_actual * paso
        y_actual, z_actual = gauss_seidel_sin_amortiguamiento(t_actual, y_actual, z_actual, paso, b, funcion_de_terreno, derivada_de_funcion_de_terreno)
        if imprimir_valores_intermedios:
            print(f"Avance número {avance_actual}, t = {t_actual}, y = {y_actual}")
    
    return y_actual


def estimar_orden_de_convergencia(paso, b, funcion_de_terreno, derivada_de_funcion_de_terreno):
    y_con_paso = resolver(paso, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
    y_con_mitad_de_paso = resolver(paso/2, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
    y_con_dieciseisavo_de_paso = resolver(paso/16, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)

    return math.log(abs(y_con_mitad_de_paso - y_con_dieciseisavo_de_paso) / abs(y_con_paso - y_con_dieciseisavo_de_paso)) / math.log(0.5)

def main():
    paso = 0.005
    b = 0.5

    # Resolver con funcion_de_terreno_constante
    funcion_de_terreno = funcion_de_terreno_constante
    derivada_de_funcion_de_terreno = derivada_de_funcion_de_terreno_constante

    start_time = time.time()
    y_resultado_constante = resolver(paso, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
    end_time = time.time()
    tiempo_constante = end_time - start_time

    # Resolver con funcion_de_terreno_con_loma_de_burro
    funcion_de_terreno = funcion_de_terreno_con_loma_de_burro
    derivada_de_funcion_de_terreno = derivada_de_funcion_de_terreno_con_loma_de_burro

    start_time = time.time()
    y_resultado_burro = resolver(paso, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
    end_time = time.time()
    tiempo_burro = end_time - start_time

    # Imprimir resultados
    print(f"Resultado con funcion_de_terreno_constante: y = {y_resultado_constante}, tiempo = {tiempo_constante} segundos")
    print(f"Resultado con funcion_de_terreno_con_loma_de_burro: y = {y_resultado_burro}, tiempo = {tiempo_burro} segundos")

    # Graficar resultados
    tiempos = [tiempo_constante, tiempo_burro]
    etiquetas = ['Constante', 'Burro']
    plt.bar(etiquetas, tiempos, color=['blue', 'green'])
    plt.title('Comparación de tiempos de ejecución')
    plt.xlabel('Tipo de función de terreno')
    plt.ylabel('Tiempo (segundos)')
    plt.show()

if __name__ == "__main__":
    main()


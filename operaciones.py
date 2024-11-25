import math

MASA = 110691 / 200
Y_INICIAL = 0
Z_INICIAL = 0
TIEMPO_FINAL = 5

CONSTANTS = {'CONSTANTE_ELASTICA': float(25000), 'CONSTANTE_AMORTIGUAMIENTO': float(0)}


def setLambda(v):
    CONSTANTS['CONSTANTE_AMORTIGUAMIENTO'] = float(v)


def setK(v):
    CONSTANTS['CONSTANTE_ELASTICA'] = float(v)


def getK():
    return CONSTANTS['CONSTANTE_ELASTICA']


def getLambda():
    return CONSTANTS['CONSTANTE_AMORTIGUAMIENTO']


def gauss_seidel(t_actual, y_actual, z_actual, paso, b, funcion_de_terreno,
                                     derivada_de_funcion_de_terreno):
    c_actual = funcion_de_terreno(t_actual)
    c_siguiente = funcion_de_terreno(t_actual + paso)
    c_siguiente_derivada = derivada_de_funcion_de_terreno(t_actual + paso)
    c_actual_derivada = derivada_de_funcion_de_terreno(t_actual)
    semilla_y, semilla_z = siguiente_valor_de_euler_explicito(c_actual, c_actual_derivada, y_actual, z_actual, paso)
    y_siguiente = semilla_y
    z_siguiente = semilla_z
    

    for _ in range(25):
        y_siguiente = y_actual + paso * ((1 - b) * z_actual + b * z_siguiente)
        z_siguiente = (1 / (1 + paso * b * CONSTANTS['CONSTANTE_AMORTIGUAMIENTO'] / MASA)) * (
                    z_actual + (paso / MASA) * (b * (
                    CONSTANTS['CONSTANTE_ELASTICA'] * (
                    c_siguiente - y_siguiente) + CONSTANTS['CONSTANTE_AMORTIGUAMIENTO'] * c_siguiente_derivada) + (
                                                        1 - b) * CONSTANTS['CONSTANTE_ELASTICA'] * (
                                                        c_actual - y_actual) + CONSTANTS['CONSTANTE_AMORTIGUAMIENTO'] * (
                                                        c_actual_derivada - z_actual)))

    return y_siguiente, z_siguiente


def siguiente_valor_de_euler_explicito(c, c_derivada, y_n, z_n, paso):
    y_siguiente = y_n + paso * z_n
    z_siguiente = z_n + paso / MASA * ( CONSTANTS['CONSTANTE_ELASTICA'] * (c - y_n) + CONSTANTS['CONSTANTE_AMORTIGUAMIENTO'] * (c_derivada - z_n)) 
    return y_siguiente, z_siguiente

def resolver(paso, b, imprimir_valores_intermedios, funcion_de_terreno, derivada_de_funcion_de_terreno):
    y_actual = Y_INICIAL
    z_actual = Z_INICIAL
    y_values = [y_actual]

    if imprimir_valores_intermedios:
        print(f"Avance número {0}, t = {0}, y = {y_actual}")

    for avance_actual in range(1, int(TIEMPO_FINAL / paso) + 1):
        t_actual = avance_actual * paso
        y_actual, z_actual = gauss_seidel(t_actual, y_actual, z_actual, paso, b, funcion_de_terreno,
                                                              derivada_de_funcion_de_terreno)
        y_values.append(y_actual)
        if imprimir_valores_intermedios:
            print(f"Avance número {avance_actual}, t = {t_actual}, y = {y_actual}")

    return y_actual, y_values


def estimar_orden_de_convergencia(paso, b, funcion_de_terreno, derivada_de_funcion_de_terreno):
    y_con_paso, _ = resolver(paso, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
    y_con_mitad_de_paso, _ = resolver(paso / 2, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)
    y_con_dieciseisavo_de_paso, _ = resolver(paso / 16, b, False, funcion_de_terreno, derivada_de_funcion_de_terreno)

    return math.log(abs(y_con_mitad_de_paso - y_con_dieciseisavo_de_paso) / abs(
        y_con_paso - y_con_dieciseisavo_de_paso)) / math.log(0.5)

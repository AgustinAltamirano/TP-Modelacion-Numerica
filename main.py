import math

MASA = 110691 / 200
CONSTANTE_ELASTICA = 25000
CONSTANTE_AMORTIGUAMIENTO = 0
Y_INICIAL = 0.5
Z_INICIAL = 0
TIEMPO_FINAL = 5

def funcion_de_terreno_constante(t):
    return 0.1

def gauss_seidel_sin_amortiguamiento(t_actual, y_actual, z_actual, paso, b):
    c_actual = funcion_de_terreno_constante(t_actual)
    c_siguiente = funcion_de_terreno_constante(t_actual + paso)
    semilla_y, semilla_z = siguiente_valor_de_euler_explicito_sin_amortiguamiento(c_actual, y_actual, z_actual, paso)
    y_siguiente = semilla_y
    z_siguiente = semilla_z

    for _ in range(25):
        y_siguiente = y_actual + paso * ((1 - b) * z_actual + b * z_siguiente)
        z_siguiente = z_actual + paso * (b * (CONSTANTE_ELASTICA / MASA) * (c_siguiente - y_siguiente) + (1 - b) * CONSTANTE_ELASTICA / MASA * (c_actual - y_actual))
    
    return y_siguiente, z_siguiente

def siguiente_valor_de_euler_explicito_sin_amortiguamiento(c, y_n, z_n, paso):
    y_siguiente = y_n + paso * z_n
    z_siguiente = z_n + paso * CONSTANTE_ELASTICA / MASA * (c - y_n)
    return y_siguiente, z_siguiente

def resolver(paso, b, imprimir_valores_intermedios):
    y_actual = Y_INICIAL 
    z_actual = Z_INICIAL

    if imprimir_valores_intermedios:
        print(f"Avance número {0}, t = {0}, y = {y_actual}")

    for avance_actual in range(1, int(TIEMPO_FINAL/paso) + 1):
        t_actual = avance_actual * paso
        y_actual, z_actual = gauss_seidel_sin_amortiguamiento(t_actual, y_actual, z_actual, paso, b)
        if imprimir_valores_intermedios:
            print(f"Avance número {avance_actual}, t = {t_actual}, y = {y_actual}")
    
    return y_actual


def estimar_orden_de_convergencia(paso, b):
    y_con_paso = resolver(paso, b, False)
    y_con_mitad_de_paso = resolver(paso/2, b, False)
    y_con_dieciseisavo_de_paso = resolver(paso/16, b, False)

    return math.log(abs(y_con_mitad_de_paso - y_con_dieciseisavo_de_paso) / abs(y_con_paso - y_con_dieciseisavo_de_paso)) / math.log(0.5)
    


def main():
    paso = 0.005
    b = 0.5

    y_resultado = resolver(paso, b, True)
    print(f"y = {y_resultado}")
    print(f"Orden de convergencia: {estimar_orden_de_convergencia(paso, b)}")

if __name__ == "__main__":
    main()
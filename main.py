def newton_rhapson(f, vi):
    pass

def gauss_seidel_sin_amortiguamiento(c, y_n, z_n, masa, constante_elastica, paso, b):
    semilla_y, semilla_z = siguiente_valor_de_euler_explicito_sin_amortiguamiento(c, y_n, z_n, masa, constante_elastica, paso)
    y_anterior = semilla_y
    z_anterior = semilla_z

    y_siguiente = 8
    z_siguiente = 8

    while abs(y_siguiente - y_anterior) > 1e-10 and abs(z_siguiente - z_anterior) > 1e-10:
       y_anterior = y_siguiente
       z_anterior = z_siguiente

       y_siguiente = y_n + paso * ((1 - b) * z_n + b * z_siguiente)
       z_siguiente = z_n + paso * (b * (constante_elastica / masa) * (c - y_siguiente) + (1 - b) * constante_elastica / masa * (c - y_n))
    
    return y_siguiente, z_siguiente

def siguiente_valor_de_euler_explicito_sin_amortiguamiento(c, y_n, z_n, masa, constante_elastica, paso):
    y_siguiente = y_n + paso * z_n
    z_siguiente = z_n + paso * (constante_elastica) / masa * (c - y_n)
    return y_siguiente, z_siguiente

def resolver():
    y_inicial = 0.5
    z_inicial = 0
    masa = 110691 / 200
    constante_elastica = 25000
    constante_amortiguamiento = 0
    c = 0.1
    tiempo_final = 5
    paso = 0.005
    b = 1

    y_actual = y_inicial 
    z_actual = z_inicial

    print(f"t: {0}, y: {y_actual}, z: {z_actual}")

    for t in range(1, int(tiempo_final/paso) + 1):
        y_actual, z_actual = gauss_seidel_sin_amortiguamiento(c, y_actual, z_actual, masa, constante_elastica, paso, b)
        print(f"t: {t}, y: {y_actual}, z: {z_actual}")



def main():
    resolver()
    """"
    y_inicial = 0.5
    z_inicial = 0
    masa = 110691 / 200
    constante_elastica = 25000
    constante_amortiguamiento = 0
    c = 0.1
    tiempo_final = 5
    paso = 0.005

    y_actual = y_inicial
    z_actual = z_inicial

    valores_y = []
    valores_z = []

    print(f"t: {0}, y: {y_actual}, z: {z_actual}")

    for t in range(1, int(tiempo_final/paso) + 1):
        y_actual, z_actual = siguiente_valor_de_euler_explicito_sin_amortiguamiento(c, y_actual, z_actual, masa, constante_elastica, paso)
        valores_y.append(y_actual)
        valores_z.append(z_actual)
        print(f"t: {t}, y: {y_actual}, z: {z_actual}")"""
    

if __name__ == "__main__":
    main()
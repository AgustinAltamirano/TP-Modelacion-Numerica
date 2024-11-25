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

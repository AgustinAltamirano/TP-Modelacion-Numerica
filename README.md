# Trabajo Pŕactico - Modelación Numérica - FIUBA 2C 2024

## Integrantes

- Agustin Altamirano (110237)
- Martín Mastropietro (108949)
- Enzo Martín Codini (110691)

## Requisitos

- [Python 3](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/) (instalable con pip3)
- [NumPy](https://numpy.org/) (instalable con pip3) 

## Uso

### Ejercicio 1

Se debe ejecutar el comando

`python3 main.py 1 <val k> <val lambda> <paso> <betas>`

Donde `<val k>` es el valor de la constante elástica, `<val_l>` el valor de la constante de amortiguamiento, y `<betas>` los valores de beta que queremos evaluar, separados por coma. Por ejemplo, para obtener los resultados pedidos en el enunciado:

`python3 main.py 1 25000 0 0.005 0,0.25,0.5,0.75,1`

Al ejecutarse, el programa muestra los gráficos y genera un archivo llamado `output.txt` con los resultados.

### Ejercicio 2

Se debe ejecutar el comando

`python3 main.py 2 <val k> <val lambda> <paso> <beta>`

Este comando solo acepta un valor para beta, especificado en el parametro `<beta>`. Por ejemplo, para obtener los resultados pedidos por el enunciado:

`python3 main.py 2 25000 750 0.005 0.5`

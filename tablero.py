import numpy as np
import random

# Tamaño del tablero y estados de las celdas
x = 25
sano = 1
infectado = 2
inmune = 3
muerto = 4
vacio = 0
refugio = 5

# Variables globales para probabilidades
probabilidad_infeccion_base = 0.25  # Probabilidad base por cada vecino infectado
probabilidad_muerte_base = 0.25     # Probabilidad base por cada vecino sano
iteraciones_para_curar = 15         # Iteraciones necesarias para curar

# Inicializar el tablero y las iteraciones de los infectados
iteracionesInfectados = np.full((x, x), vacio)
tablero = np.full((x, x), vacio)

def actualizar(tablero):
    nuevoTablero = np.copy(tablero)
    num_infectados = 0
    num_sanos = 0

    # Revisar las celdas alrededor de cada persona
    for i in range(x):
        for j in range(x):
            # Contar cuántas iteraciones sobrevive un infectado
            if tablero[i, j] == infectado:
                iteracionesInfectados[i, j] += 1
                if iteracionesInfectados[i, j] == iteraciones_para_curar:
                    nuevoTablero[i, j] = inmune
                    continue

            # Contar infectados alrededor
            num_infectados = sum([
                tablero[i, (j - 1) % x] == infectado,
                tablero[i, (j + 1) % x] == infectado,
                tablero[(i - 1) % x, j] == infectado,
                tablero[(i - 1) % x, (j - 1) % x] == infectado,
                tablero[(i - 1) % x, (j + 1) % x] == infectado,
                tablero[(i + 1) % x, j] == infectado,
                tablero[(i + 1) % x, (j - 1) % x] == infectado,
                tablero[(i + 1) % x, (j + 1) % x] == infectado
            ])

            # Contar sanos alrededor
            num_sanos = sum([
                tablero[i, (j - 1) % x] == sano,
                tablero[i, (j + 1) % x] == sano,
                tablero[(i - 1) % x, j] == sano,
                tablero[(i - 1) % x, (j - 1) % x] == sano,
                tablero[(i - 1) % x, (j + 1) % x] == sano,
                tablero[(i + 1) % x, j] == sano,
                tablero[(i + 1) % x, (j - 1) % x] == sano,
                tablero[(i + 1) % x, (j + 1) % x] == sano
            ])

            # Probabilidad de infectarse (escala según los infectados alrededor)
            if tablero[i, j] == sano:
                probabilidad_infeccion = min(1, num_infectados * probabilidad_infeccion_base)
                if random.random() < probabilidad_infeccion:
                    nuevoTablero[i, j] = infectado

            # Probabilidad de morir de un infectado (escala según los sanos alrededor)
            if tablero[i, j] == infectado:
                probabilidad_muerte = min(1, num_sanos * probabilidad_muerte_base)
                if random.random() < probabilidad_muerte:
                    nuevoTablero[i, j] = muerto

            # Movimiento de las celdas solo hacia izquierda, derecha, arriba, abajo
            estado = tablero[i, j]
            prob = random.random()

            # Movilidad de los infectados e inmunes
            if estado == infectado or estado == inmune:
                if 0 <= (j - 1) < x and prob < 0.25 and tablero[i, j - 1] == vacio and nuevoTablero[i, j - 1] == vacio:
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i, j - 1] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i, j - 1] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0
                if 0 <= (j + 1) < x and 0.25 <= prob < 0.50 and tablero[i, j + 1] == vacio and nuevoTablero[i, j + 1] == vacio:
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i, j + 1] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i, j + 1] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0
                if 0 <= (i - 1) < x and 0.50 <= prob < 0.75 and tablero[i - 1, j] == vacio and nuevoTablero[i - 1, j] == vacio:
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i - 1, j] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i - 1, j] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0
                if 0 <= (i + 1) < x and 0.75 <= prob and tablero[i + 1, j] == vacio and nuevoTablero[i + 1, j] == vacio:
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i + 1, j] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i + 1, j] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0

            # Movilidad de los sanos
            if estado == sano:
                if 0 <= (j - 1) < x and prob < 0.25 and (tablero[i, j - 1] == vacio or tablero[i, j - 1] == refugio) and (nuevoTablero[i, j - 1] == vacio or nuevoTablero[i, j - 1] == refugio):
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i, j - 1] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i, j - 1] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0
                if 0 <= (j + 1) < x and 0.25 <= prob < 0.50 and (tablero[i, j + 1] == vacio or tablero[i, j + 1] == refugio) and (nuevoTablero[i, j + 1] == vacio or nuevoTablero[i, j + 1] == refugio):
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i, j + 1] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i, j + 1] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0
                if 0 <= (i - 1) < x and 0.50 <= prob < 0.75 and (tablero[i - 1, j] == vacio or tablero[i - 1, j] == refugio) and (nuevoTablero[i - 1, j] == vacio or nuevoTablero[i - 1, j] == refugio):
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i - 1, j] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i - 1, j] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0
                if 0 <= (i + 1) < x and 0.75 <= prob and (tablero[i + 1, j] == vacio or tablero[i + 1, j] == refugio) and (nuevoTablero[i + 1, j] == vacio or nuevoTablero[i + 1, j] == refugio):
                    nuevoTablero[i, j] = vacio
                    nuevoTablero[i + 1, j] = estado
                    if tablero[i, j] == infectado:
                        iteracionesInfectados[i + 1, j] = iteracionesInfectados[i, j]
                        iteracionesInfectados[i, j] = 0

            num_infectados = 0
            num_sanos = 0

    return nuevoTablero

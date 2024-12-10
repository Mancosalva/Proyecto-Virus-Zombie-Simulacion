import tkinter as tk
import numpy as np
from tablero import actualizar, tablero, x, sano, infectado, inmune, muerto, vacio,probabilidad_infeccion_base, probabilidad_muerte_base, iteraciones_para_curar
from tablero import probabilidad_infeccion_base, probabilidad_muerte_base, iteraciones_para_curar

root = tk.Tk()
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)
root.resizable(0, 0)

# Definir una variable para almacenar la ventana de configuración
config_window = None

# Crear la ventana de configuración antes de iniciar la simulación
def ventana_configuracion():
    global config_window
    if config_window is not None and config_window.winfo_exists():  # Verificar si la ventana ya está abierta
        return  # Si la ventana ya está abierta, no hacer nada

    config_window = tk.Toplevel(root)
    config_window.title("Configuración de la simulación")

    # Función para actualizar las variables globales con los valores de los sliders
    def actualizar_parametros():
        global probabilidad_infeccion_base, probabilidad_muerte_base, iteraciones_para_curar
        probabilidad_infeccion_base = slider_infeccion.get()
        probabilidad_muerte_base = slider_muerte.get()
        iteraciones_para_curar = slider_iteraciones.get()
        config_window.destroy()  # Cierra la ventana de configuración

    # Sliders para controlar los parámetros
    slider_infeccion = tk.Scale(config_window, from_=0, to=1, resolution=0.01, orient='horizontal', label='Prob. base infección')
    slider_infeccion.set(probabilidad_infeccion_base)
    slider_infeccion.grid(row=0, column=0, columnspan=2)

    slider_muerte = tk.Scale(config_window, from_=0, to=1, resolution=0.01, orient='horizontal', label='Prob. base muerte')
    slider_muerte.set(probabilidad_muerte_base)
    slider_muerte.grid(row=1, column=0, columnspan=2)

    slider_iteraciones = tk.Scale(config_window, from_=1, to=50, resolution=1, orient='horizontal', label='Iteraciones para curar')
    slider_iteraciones.set(iteraciones_para_curar)
    slider_iteraciones.grid(row=2, column=0, columnspan=2)

    # Botón para aplicar los valores y cerrar la ventana de configuración
    boton_iniciar = tk.Button(config_window, text='Iniciar simulación', command=actualizar_parametros)
    boton_iniciar.grid(row=3, column=0, columnspan=2)

    # Botón para salir sin iniciar la simulación
    boton_salir = tk.Button(config_window, text='Salir', command=config_window.destroy)
    boton_salir.grid(row=4, column=0, columnspan=2)

    config_window.mainloop()

# Funciones de la simulación
def click(i, j, tablero, botones):
    if tablero[i, j] == 0: tablero[i, j] = 1
    elif tablero[i, j] == 1: tablero[i, j] = 2
    elif tablero[i, j] == 2: tablero[i, j] = 5
    elif tablero[i, j] == 5: tablero[i, j] = 0

    if tablero[i, j] == 1: color = 'white'
    elif tablero[i, j] == 2: color = 'red'
    elif tablero[i, j] == 3: color = 'blue'
    elif tablero[i, j] == 4: color = 'black'
    elif tablero[i, j] == 5: color = 'yellow'
    else: color = 'grey'
    botones[i][j].config(bg=color)

botones = []
for i in range(x):
    row = []
    for j in range(x):
        if tablero[i, j] == 1: color = 'white'
        elif tablero[i, j] == 2: color = 'red'
        elif tablero[i, j] == 3: color = 'blue'
        elif tablero[i, j] == 4: color = 'black'
        elif tablero[i, j] == 5: color = 'yellow'
        else: color = 'grey'
        boton = tk.Button(
            root,
            command=lambda i=i, j=j: click(i, j, tablero, botones),
            height=1,
            width=2,
            bg=color
        )
        row.append(boton)
    botones.append(row)

for i in range(x):
    for j in range(x):
        botones[i][j].grid(row=i, column=j, sticky="nsew")

def gui_update():
    global tablero
    tablero = actualizar(tablero)
    for i in range(x):
        for j in range(x):
            if tablero[i, j] == 1: color = 'white'
            elif tablero[i, j] == 2: color = 'red'
            elif tablero[i, j] == 3: color = 'blue'
            elif tablero[i, j] == 4: color = 'black'
            elif tablero[i, j] == 5: color = 'yellow'
            else: color = 'grey'
            botones[i][j].config(bg=color)
    if running:
        root.after(speed_dict[speed_var.get()], gui_update)

def iniciar():
    global running
    running = True
    gui_update()

def reiniciar():
    global tablero
    limpiar()  # Limpiar el tablero antes de reiniciar
    ventana_configuracion()  # Reabrir la ventana de configuración para cambiar los valores
    iniciar()  # Iniciar la simulación con los nuevos valores

def parar():
    global running
    running = False

def step():
    if not running:
        gui_update()

def limpiar():
    global tablero
    parar()
    tablero = np.full((x, x), vacio)
    for i in range(x):
        for j in range(x):
            botones[i][j].config(bg='grey')

# Botón para mostrar la ventana de configuración
boton_configuracion = tk.Button(root, text='Configuración', command=ventana_configuracion)
boton_configuracion.grid(row=x, column=0, columnspan=x // 5, sticky="we")

# Botones de control de simulación
boton_iniciar = tk.Button(root, text='Iniciar simulación', command=iniciar)
boton_iniciar.grid(row=x, column=1, columnspan=x // 5, sticky="we")

boton_parar = tk.Button(root, text='Parar simulación', command=parar)
boton_parar.grid(row=x, column=2, columnspan=x // 5, sticky="we")

boton_step = tk.Button(root, text='Paso', command=step)
boton_step.grid(row=x, column=3, columnspan=x // 5, sticky="we")

boton_limpiar = tk.Button(root, text='Limpiar', command=limpiar)
boton_limpiar.grid(row=x, column=4, columnspan=x // 5, sticky="we")

# Botón para reiniciar la simulación con los valores actuales de los sliders
boton_reiniciar = tk.Button(root, text='REINICIAR', command=reiniciar)
boton_reiniciar.grid(row=x, column=5 * (x // 5), columnspan=x // 5, sticky="we")

# Velocidad de ejecución
speed_dict = {'Lento': 500, 'Normal': 200, 'Rápido': 10}
speed_var = tk.StringVar(root)
speed_var.set('Normal')
speed_option = tk.OptionMenu(root, speed_var, *speed_dict.keys())
speed_option.grid(row=x, column=6 * (x // 5), columnspan=x // 5, sticky="we")

# Ejecutar la interfaz
root.mainloop()

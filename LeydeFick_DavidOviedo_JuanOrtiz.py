import tkinter as tk
import numpy as np
from tkinter import Toplevel
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)




def jacobi_method(A, b, tolerance=1e-6):
    """
    Implementación del método de Jacobi para resolver un sistema de ecuaciones lineales Ax = b.

    Args:
        A (numpy.ndarray): Matriz de coeficientes del sistema.
        b (numpy.ndarray): Vector de términos independientes.
        tolerance (float, optional): Tolerancia para determinar la convergencia del método. Valor por defecto es 1e-6.

    Returns:
        numpy.ndarray: Vector solución x del sistema de ecuaciones.
    """

    n = len(b)
    x = np.zeros_like(b)
    x_new = np.zeros_like(b)

    while True:
        for i in range(n):
            # Calculamos el término de suma
            sum_term = np.dot(A[i, :i], x[:i]) + np.dot(A[i, i+1:], x[i+1:])
            # Calculamos el nuevo valor de x
            x_new[i] = (b[i] - sum_term) / A[i, i]

        if np.linalg.norm(x - x_new) < tolerance:
            break

        x = x_new.copy()

    return x

def generar_matriz(alpha, tamaño_paso, nodos):
    """
    Genera una matriz tridiagonal simétrica utilizada en la ley de Fick Estable

    Args:
        alpha (float): Coeficiente de difusión.
        tamaño_paso (float): Tamaño del paso espacial.
        nodos (int): Número de nodos.

    Returns:
        numpy.ndarray: Matriz generada.
    """

    Y = alpha**2 * (tamaño_paso**2)
    tamaño_matriz = int(nodos) - 1
    matriz = np.zeros((tamaño_matriz, tamaño_matriz))

    for i in range(tamaño_matriz):
        matriz[i, i] = -2 - Y
        if i < tamaño_matriz - 1:
            matriz[i, i + 1] = 1
            matriz[i + 1, i] = 1

    matriz[len(matriz)-1, len(matriz)-2] = 2

    return matriz


def generar_vector_b(tamaño_matriz, parametro):
    """
    Genera el vector b utilizado en la Ley de Fick estable.

    Args:
        tamaño_matriz (int): Tamaño de la matriz.
        parametro (int): Parámetro utilizado para generar el vector b.

    Returns:
        numpy.ndarray: Vector b generado.
    """

    vector_b = np.zeros((tamaño_matriz, 1))
    vector_b[0] = -int(parametro)
    return vector_b

def metodo_diferencias_finitas_estable(param1, param3, param4, param5):
    # Se crea una ventana emergente (popup) utilizando tkinter
    popup = Toplevel(root)

    # Se genera la matriz A utilizando la función generar_matriz, pasando los parámetros correspondientes
    matriz_A = generar_matriz(float(param4), int(param1) / int(param3), param3)

    # Se genera el vector B utilizando la función generar_vector_b, pasando los parámetros correspondientes
    vector_B = generar_vector_b(int(param3) - 1, param5)

    # Se utiliza el método de Jacobi para resolver el sistema de ecuaciones lineales
    x = jacobi_method(matriz_A, vector_B)

    # Se crea un array T de valores equiespaciados entre 0 y param1, con param3-1 elementos
    T = np.linspace(0, int(param1), int(param3) - 1)

    # Se crea una figura 
    fig = Figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111)

    # Se traza la gráfica de T vs x utilizando los valores calculados
    ax.plot(T, x)

    # Se establece un título para la figura
    fig.suptitle('Gráfico de T vs X')

    # Se establecen etiquetas para los ejes x e y
    ax.set_xlabel('x')
    ax.set_ylabel('T')

    # Se desactiva la notación científica para el eje y
    ax.yaxis.get_major_formatter().set_scientific(False)

    # Se desactiva el uso de offset para el eje y
    ax.yaxis.get_major_formatter().set_useOffset(False)

    # Se activa el grid
    ax.grid(True)

    # Se ajusta la figura para que se ajuste al plot
    fig.tight_layout()

    # Se crea un canvas y se dibuja la grafica en el
    canvas = FigureCanvasTkAgg(fig, master=popup)
    canvas.draw()

    # Se empaqueta el lienzo de dibujo en la ventana emergente
    canvas.get_tk_widget().pack()





def abrir_ley_fick_estable():
    # Función para abrir la página de la Ley de Fick estable


    # Limpiar el contenido actual
    limpiar_contenido()

    # Agregar contenido para la página de la Ley de Fick estable
    label = tk.Label(root, text="Introduce los parámetros para la Ley de Fick: Estable")
    label.pack(pady=10)
    label1 = tk.Label(root, text="Longitud de la superficie de difusión:")
    label1.pack()
    entrada_1 = tk.Entry(root)
    entrada_1.pack()


    label3 = tk.Label(root, text="Número de nodos en el espacio:")
    label3.pack()
    entrada_3 = tk.Entry(root)
    entrada_3.pack()

    label4 = tk.Label(root, text="Constante de material:")
    label4.pack()
    entrada_4 = tk.Entry(root)
    entrada_4.pack()

    label5 = tk.Label(root, text="Temperatura del contorno (condición de frontera):")
    label5.pack()
    entrada_5 = tk.Entry(root)
    entrada_5.pack()


    def recibir_parametros():

        param1 = entrada_1.get()
        param3 = entrada_3.get()
        param4 = entrada_4.get()
        param5 = entrada_5.get()

        metodo_diferencias_finitas_estable(param1, param3, param4, param5)



    boton_enviar = tk.Button(root, text="Enviar", command=recibir_parametros)
    boton_enviar.pack()


def calcular_fick_transitorio(longitud, t_total, num_nodos_espacio, num_nodos_tiempo, mconst, temp_contorno, temp_inicial):
    # Calcular tamaño de paso
    dx = longitud / num_nodos_espacio
    dt = t_total / num_nodos_tiempo

    # Calcular constantes
    alpha = np.sqrt(mconst * dt / dx**2)

    # Crear matriz A y vector B
    numero_desconocidas = num_nodos_espacio - 1
    numero_ecuaciones = numero_desconocidas * num_nodos_tiempo

    # Generar la matriz A utilizando la función generar_matriz_A, pasando los parámetros correspondientes
    A = generar_matriz_A(longitud, t_total, num_nodos_espacio, num_nodos_tiempo, alpha)

    # Generar el vector B utilizando la función generar_matriz_B, pasando los parámetros correspondientes
    b = generar_matriz_B(longitud, t_total, num_nodos_espacio, num_nodos_tiempo, temp_contorno, temp_inicial)

    # Inicializar vectores de solución
    x = np.zeros(numero_ecuaciones)
    x_new = np.copy(x)

    max_iterations = 1000
    tolerance = 1e-6

    # Resolver el sistema de ecuaciones utilizando el método de Jacobi
    for iteration in range(max_iterations):
        for i in range(numero_ecuaciones):
            x_new[i] = (b[i] - np.dot(A[i, :], x) + A[i, i] * x[i]) / A[i, i]

        # Verificar la convergencia utilizando la norma euclidiana de la diferencia entre las soluciones
        if np.linalg.norm(x_new - x) < tolerance:
            break

        x = np.copy(x_new)

    # Reorganizar el vector solución en una matriz de tamaño (num_nodos_tiempo, numero_desconocidas)
    return x.reshape((num_nodos_tiempo, numero_desconocidas))



def generar_matriz_A(longitud, t_total, num_nodos_espacio, num_nodos_tiempo, alpha):
    # Calcular los tamaños de paso
    delta_x = float(longitud) / float(num_nodos_espacio)
    delta_t = float(t_total) / float(num_nodos_tiempo)

    # Calcular el número de incógnitas
    N = int(num_nodos_espacio) - 1

    # Crear una matriz de ceros de tamaño (N * num_nodos_tiempo) x (N * num_nodos_tiempo)
    A = np.zeros((N * int(num_nodos_tiempo), N * int(num_nodos_tiempo)))

    # Definir los coeficientes B0, B1 y B2
    B0 = delta_t
    B1 = -2 * (delta_x**2) - delta_t + (delta_x**2) * alpha**2
    B2 = delta_t

    # Rellenar la matriz A con los coeficientes correspondientes
    for i in range(N * int(num_nodos_tiempo)):
        A[i, i] = B1

        if i >= N:
            A[i, i - N] = B0

        if i < (num_nodos_tiempo - 1) * N:
            A[i, i + N] = B2

        if (i + 1) % N != 0:
            A[i, i + 1] = delta_x**2

        if i % N != 0:
            A[i, i - 1] = delta_x**2

    return A



def generar_matriz_B(longitud, t_total, num_nodos_espacio, num_nodos_tiempo, temp_contorno, temp_inicial):
    # Calcular los tamaños de paso
    delta_x = float(longitud) / float(num_nodos_espacio)
    delta_t = float(t_total) / float(num_nodos_tiempo)

    # Calcular el número de incógnitas
    N = int(num_nodos_espacio) - 1

    # Crear un vector de ceros de tamaño N * num_nodos_tiempo
    b = np.zeros(N * int(num_nodos_tiempo))

    # Definir los coeficientes B2 y B3
    B2 = delta_t
    B3 = -delta_x ** 2

    # Rellenar el vector b con los valores correspondientes
    for j in range(int(num_nodos_tiempo)):
        for i in range(N):
            if i == 0:
                b[j * N + i] = (j + 1) * B2
            else:
                b[j * N + i] = j * B3

    # Aplicar las condiciones de contorno
    b[0] -= temp_contorno
    b[N * (num_nodos_tiempo - 1)] -= temp_inicial

    return b






def abrir_ley_fick_transitorio():
    # Función para abrir la página de la Ley de Fick transitoria
    # Reemplazar con tu propia implementación

    # Limpiar el contenido actual
    limpiar_contenido()

    # Agregar contenido para la página de la Ley de Fick transitoria
    label = tk.Label(root, text="Introduce los parámetros para la Ley de Fick: Transitorio")
    label.pack(pady=10)
    label1 = tk.Label(root, text="Longitud de la superficie de difusión:")
    label1.pack()
    entrada_1 = tk.Entry(root)
    entrada_1.pack()

    label2 = tk.Label(root, text="Tiempo total de la simulacion:")
    label2.pack()
    entrada_2= tk.Entry(root)
    entrada_2.pack()

    label3 = tk.Label(root, text="Número de nodos en el espacio:")
    label3.pack()
    entrada_3 = tk.Entry(root)
    entrada_3.pack()

    label4 = tk.Label(root, text="Constante de material:")
    label4.pack()
    entrada_4 = tk.Entry(root)
    entrada_4.pack()

    label5 = tk.Label(root, text="Temperatura del contorno (condición de frontera):")
    label5.pack()
    entrada_5 = tk.Entry(root)
    entrada_5.pack()

    label6= tk.Label(root, text="Temperatura inicial")
    label6.pack()
    entrada_6 = tk.Entry(root)
    entrada_6.pack()

    label7 = tk.Label(root, text="Numero de nodos en el tiempo:")
    label7.pack()
    entrada_7 = tk.Entry(root)
    entrada_7.pack()
    def recibir_parametros():

        param1 = float(entrada_1.get())
        param2 = float(entrada_2.get())
        param3 = int(entrada_3.get())
        param4 = float(entrada_4.get())
        param5 = float(entrada_5.get())
        param6 = float(entrada_6.get())
        param7 = int(entrada_7.get())

        solucion = np.array(calcular_fick_transitorio(param1, param2, param3, param7, param4, param5, param6))


        x_valores = np.linspace(0, param1, param3 - 1)


        popup = Toplevel(root)
        fig = Figure(figsize=(5, 5), dpi=100)
        ax = fig.add_subplot(111)
        for i in range(param7):
            ax.plot(x_valores, -solucion[i, :], label=f'Tiempo {i+1}')
        fig.suptitle('Grafico de T vs X')
        ax.set_xlabel('Posicion')
        ax.set_ylabel('T')

        canvas = FigureCanvasTkAgg(fig, master=popup)
        canvas.draw()
        canvas.get_tk_widget().pack()

    boton_enviar = tk.Button(root, text="Enviar", command=recibir_parametros)
    boton_enviar.pack()

def limpiar_contenido():
    # Función para limpiar el contenido actual en la ventana
    for widget in root.winfo_children():
        widget.pack_forget()

# Crear la ventana principal
root = tk.Tk()
root.title("Ley de Fick")

# Agregar texto del título
title_label = tk.Label(root, text="Ley de Fick: Selecciona la opción que necesites.", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)

# Agregar texto del subtítulo
subtitle_label = tk.Label(root, text="David Oviedo y Juan Ortiz", font=("Helvetica", 12))
subtitle_label.pack(pady=5)

# Crear los botones
boton_ley_fick_estable = tk.Button(root, text="Ley de Fick: Estable", command=abrir_ley_fick_estable)
boton_ley_fick_estable.pack(pady=10)

boton_ley_fick_transitorio = tk.Button(root, text="Ley de Fick: Transitorio", command=abrir_ley_fick_transitorio)
boton_ley_fick_transitorio.pack(pady=10)

# Ejecutar el ciclo principal de eventos
root.mainloop()

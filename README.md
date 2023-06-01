# Ley de Fick

Este proyecto implementa la Ley de Fick utilizando el método de diferencias finitas. Proporciona soluciones tanto para el caso estacionario como para el caso transitorio de la Ley de Fick.

## Requisitos

El proyecto requiere que se instalen las siguientes bibliotecas de Python:
- Tkinter
- Numpy
- Matplotlib

Puedes instalar estas bibliotecas usando pip:


## Uso
Para ejecutar el programa, simplemente ejecuta el archivo ley_de_fick.py en Python. Aparecerá una ventana con dos opciones: "Ley de Fick: Estable" y "Ley de Fick: Transitorio".

#### Ley de Fick: Estable
En esta opción, se solicitarán los siguientes parámetros:

Longitud de la superficie de difusión: Introduce la longitud de la superficie donde se aplicará la Ley de Fick.
Número de nodos en el espacio: Introduce el número de nodos (puntos discretos) en el espacio.
Constante de material: Introduce la constante de material para el cálculo de la Ley de Fick.
Temperatura del contorno (condición de frontera): Introduce la temperatura del contorno para la Ley de Fick.
Después de proporcionar estos parámetros, se generará un gráfico que muestra la distribución de temperatura a lo largo del espacio.

#### Ley de Fick: Transitorio
En esta opción, se solicitarán los siguientes parámetros:

Longitud de la superficie de difusión: Introduce la longitud de la superficie donde se aplicará la Ley de Fick.
Tiempo total de la simulación: Introduce el tiempo total para la simulación de la Ley de Fick.
Número de nodos en el espacio: Introduce el número de nodos (puntos discretos) en el espacio.
Constante de material: Introduce la constante de material para el cálculo de la Ley de Fick.
Temperatura del contorno (condición de frontera): Introduce la temperatura del contorno para la Ley de Fick.
Temperatura inicial: Introduce la temperatura inicial para la Ley de Fick.
Número de nodos en el tiempo: Introduce el número de nodos (puntos discretos) en el tiempo.
Después de proporcionar estos parámetros, se generará un gráfico que muestra la evolución de la temperatura a lo largo del tiempo y el espacio.


"Ejercicio 1"
import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos

    # Regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    return integral

# Función de ejemplo
def funcion(x):
    return 200 * x  # Cambiar esta función según el problema

# Parámetros de integración
a, b = 0.1, 0.3  # Intervalo

# Bucle para calcular y graficar para diferentes valores de n
for n in [6, 10, 20, 30]:
    # Aproximación de la integral
    resultado = simpson_rule(funcion, a, b, n)
    print(f"La aproximación de la integral con n={n} subintervalos es: {resultado}")

    # Gráfica de la función y la aproximación con la regla de Simpson
    x_vals = np.linspace(a, b, 100)
    y_vals = funcion(x_vals)

    plt.plot(x_vals, y_vals, label=r"$f(x) = kx$", color="blue")
    plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label="Área aproximada")
    plt.scatter(np.linspace(a, b, n + 1), funcion(np.linspace(a, b, n + 1)), color="red", label="Puntos de interpolación")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.title(f"Aproximación de la integral con la regla de Simpson (n={n})")
    plt.grid()

    # Guardar la figura
    plt.savefig(f"simpson_n{n}.png")
    plt.show()

"Ejercicio 2"

import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)

    # Aplicamos la regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    return integral

# Definir la función V(t)
def funcion(t):
    return 100 * np.exp(-2 * t)

# Parámetros
a, b = 0, 5  # Intervalo [0, 5]
capacitancia = 1e-6  # Capacitancia en Faradios

# Bucle para calcular y graficar con diferentes valores de n
for n in [6, 10, 20, 30]:
    # Calcular la carga almacenada
    carga = capacitancia * simpson_rule(funcion, a, b, n)
    print(f"La aproximación de la integral usando la regla de Simpson con n={n} es: {carga:.6e} C")

    # Visualización de la función V(t) y el área aproximada
    x_vals = np.linspace(a, b, 100)
    y_vals = funcion(x_vals)

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=r"$V(t) = 100e^{-2t}$", color="blue")
    plt.fill_between(x_vals, y_vals, alpha=0.3, color="cyan", label=f"Área aproximada (n={n})")
    plt.scatter(np.linspace(a, b, n + 1), funcion(np.linspace(a, b, n + 1)), color="red", label="Puntos de interpolación")
    plt.xlabel("Tiempo (t)")
    plt.ylabel("Voltaje (V)")
    plt.title(f"Aproximación de la integral con la regla de Simpson (n={n})")
    plt.legend()
    plt.grid()

    # Guardar cada gráfica
    plt.savefig(f"simpson_n{n}.png")
    plt.show()

import numpy as np
import matplotlib.pyplot as plt

def simpson_rule(f, a, b, n):
    """Aproxima la integral de f(x) en [a, b] usando la regla de Simpson."""
    if n % 2 == 1:
        raise ValueError("El número de subintervalos (n) debe ser par.")

    h = (b - a) / n
    x = np.linspace(a, b, n + 1)  # Puntos del intervalo
    fx = f(x)  # Evaluamos la función en esos puntos

    # Aplicamos la regla de Simpson
    integral = (h / 3) * (fx[0] + 2 * np.sum(fx[2:n:2]) + 4 * np.sum(fx[1:n:2]) + fx[n])
    return integral

# Derivada de la función de temperatura dT/dx
def dT_dx(x):
    return -100 * x  # Derivada de T(x) = 300 - 50x^2

# Parámetros del problema
k = 0.5  # Conductividad térmica en W/m·K
x1, x2 = 0, 2  # Intervalo [x1, x2]

# Bucle para calcular la integral y graficar para diferentes valores de n
for n in [6, 10, 20, 30]:
    # Cálculo del flujo de calor
    Q = k * simpson_rule(dT_dx, x1, x2, n)
    print(f"n={n}: Flujo de calor Q={Q:.6f} W")

    # Visualización gráfica del flujo de calor
    x_vals = np.linspace(x1, x2, 100)  # Valores para la curva
    dT_vals = dT_dx(x_vals)  # Derivada de la temperatura

    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, dT_vals, label=r"$\frac{dT}{dx} = -100x$", color="blue")
    plt.fill_between(x_vals, dT_vals, alpha=0.3, color="cyan", label=f"Área aproximada (n={n})")
    plt.scatter(np.linspace(x1, x2, n + 1), dT_dx(np.linspace(x1, x2, n + 1)), color="red", label="Puntos de interpolación")
    plt.xlabel("x (m)")
    plt.ylabel(r"$\frac{dT}{dx}$ (K/m)")
    plt.title(f"Aproximación de la integral con la regla de Simpson (n={n})")
    plt.legend()
    plt.grid()

    # Guardar la figura
    plt.savefig(f"flujo_calor_n{n}.png")
    plt.show()

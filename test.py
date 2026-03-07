import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x, n = sp.symbols('x n', real=True)

# Verificación simbólica para n entero específico
n_val = 4

lhs = (sp.cosh(x) + sp.sinh(x))**n_val
rhs = sp.cosh(n_val*x) + sp.sinh(n_val*x)

check = sp.simplify(lhs - rhs)
print("Simplificación simbólica (debe ser 0):", check)

# Verificación gráfica
f_lhs = sp.lambdify(x, lhs, "numpy")
f_rhs = sp.lambdify(x, rhs, "numpy")

xs = np.linspace(-2, 2, 400)

plt.plot(xs, f_lhs(xs), label="LHS")
plt.plot(xs, f_rhs(xs), linestyle="dashed", label="RHS")
plt.title("Verificación gráfica de la identidad")
plt.legend()
plt.grid(True)
plt.show()
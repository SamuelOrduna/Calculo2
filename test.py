import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# ---- Definición simbólica ----
x = sp.Symbol('x', real=True)
f = sp.log(1 + x**2, 2)  # log base 2

# a) Dominio (SymPy lo maneja, pero verificamos argumento positivo)
arg = 1 + x**2
domain_condition = sp.solve_univariate_inequality(arg > 0, x)
print("Condición de dominio (arg>0):", domain_condition)

# b) Imagen: verificamos mínimo y tendencia
f_simplified = sp.simplify(f)
print("f(x) =", f_simplified)

# Samuel Orduña - 207739

# c) Intersecciones
x_intercepts = sp.solve(sp.Eq(f, 0), x)
y_intercept = f.subs(x, 0)
print("Intersección con eje x:", x_intercepts)
print("Intersección con eje y: (0, f(0)) =", (0, y_intercept))

# d) Puntos críticos
fp = sp.diff(f, x)
crit = sp.solve(sp.Eq(fp, 0), x)
print("f'(x) =", sp.simplify(fp))
print("Puntos críticos (f'=0):", crit)
print("Valor en el crítico:", [(c, sp.simplify(f.subs(x, c))) for c in crit])

# e) Límites al infinito
lim_pos = sp.limit(f, x, sp.oo)
lim_neg = sp.limit(f, x, -sp.oo)
print("lim x->+∞ f(x) =", lim_pos)
print("lim x->-∞ f(x) =", lim_neg)

# ---- Gráfica ----
xx = np.linspace(-6, 6, 1200)
ff = np.log2(1 + xx**2)

plt.figure()
plt.axhline(0)
plt.axvline(0)
plt.plot(xx, ff)
plt.title(r"$f(x)=\log_2(1+x^2)$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-0.5, max(ff)*1.05)
plt.show()
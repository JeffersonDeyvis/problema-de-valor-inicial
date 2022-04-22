# This code calculates the ODE solution.
import matplotlib.pyplot as plt
import numpy as np

# ODE example


def f(t, y):
    return np.sin(t) - t * y


# runge kutta 4th order
def rk4(f, h, t0, y0, tf):
    t = t0
    y = [y0]
    T = [t0]
    index = 0
    while t < tf:
        k1 = f(t, y[index])
        k2 = f(t + h / 2, y[index] + k1 * h / 2)
        k3 = f(t + h / 2, y[index] + k2 * h / 2)
        k4 = f(t + h, y[index] + k3 * h)
        y.append(y[index] + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4))
        t += h
        index += 1
        T.append(t)
    return (T, y)


x, y = rk4(f, 0.01, 0, 4, 20)
plt.plot(x, y)
plt.savefig('teste.png')

"""
df = pd.DataFrame({"x":x, "y":y})
df.to_csv("datapy.dat", index=False, header=False, sep=" ")
"""

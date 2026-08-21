import numpy as np

def f(x):
    return x**3-x-2
def df(x):
    return 3*x**2-1

def newton_raphson(x0):
    x=x0
    for i in range(50):
        step = f(x)/df(x)
        x=x-step

        if np.abs(step) < 1e-6:
            return x

root = newton_raphson(2)

print(f"{root:.6f}")

from scipy.optimize import fsolve
import numpy as np

Re = 1e5
e_D = 0.0002

def colebrook(f):
    return (1/np.sqrt(f))+2*np.log10((e_D/3.7)+2.51/(Re*np.sqrt(f)))
f0 = 0.02
solution = fsolve(colebrook, f0)

print(f"The friction factor f = {solution[0]:.4f}")
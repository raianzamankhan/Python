import numpy as np
from scipy.optimize import fsolve

P = 2 #bar
K1 = 0.4
K2 = 1.2

def system(vars):
    e1, e2 = vars
    eq1 = ((e1-e2)*e1*P)/((1-e1)*(1+e1)) - K1
    eq2 = (e2/(e1-e2)) - K2
    return [eq1,eq2]

e1, e2 = fsolve(system, [.3,.1])
print(f"The extent of first reaction e1 = {e1:.4f}")
print(f"The extent of second reaction e2 = {e2:.4f}")

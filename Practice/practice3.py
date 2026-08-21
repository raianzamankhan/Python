import matplotlib.pyplot as plt

Q = 10
A = 70
R = 0.5

def dH_dt(t,H):
    return ((Q-H/R)/A)

t = 0
H = 10

tf = 60
h = 0.2
steps = int((tf-t)/h)

t_list=[t]
H_list=[H]

for step in range(steps):
    slope = dH_dt(t,H)
    H+=slope*h
    t+=h
    t_list.append(t)
    H_list.append(H)

plt.plot(t_list,H_list)
plt.show()
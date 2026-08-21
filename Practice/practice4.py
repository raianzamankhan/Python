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
    m1 = dH_dt(t,H)
    m2 = dH_dt(t+h/2, H+(h/2)*m1)
    m3 = dH_dt(t+h/2, H+(h/2)*m2)
    m4 = dH_dt(t+h, H+h*m3)
    avg_slope = (m1+2*(m2+m3)+m4)/6
    H+=avg_slope*h
    t+=h
    t_list.append(t)
    H_list.append(H)

plt.plot(t_list,H_list)
plt.show()
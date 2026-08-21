import matplotlib.pyplot as plt

def dh_dt(t, h):
    if t<300:
        return ((t**(0.5)-25*h)/1000)
    else:
        return ((t**(0.5)-25*h-4)/1000)

t=0
h=0

tf=600
step_size=0.1
steps=int((tf-t)/step_size)

T=[t]
H=[h]

for step in range(steps):
    m1 = dh_dt(t,h)
    m2 = dh_dt(t+step_size/2, h+((step_size/2)*m1))
    m3 = dh_dt(t+step_size/2, h+((step_size/2)*m2))
    m4 = dh_dt(t+step_size, h+(step_size)*m3)
    avg_slope = (m1+2*(m2+m3)+m4)/6
    h += avg_slope*step_size
    t += step_size
    H.append(h*100)
    T.append(t)
    if round(t, 5) == 300:
        print(f"At t = 5 mins, h = {h*100:.4f} cm")

print(f"At t = 10 mins, h = {h*100:.4f} cm")

plt.plot(T,H)
plt.xlabel("Time (s)")
plt.ylabel("Height (cm)")
plt.grid()
plt.show()
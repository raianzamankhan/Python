import matplotlib.pyplot as plt

def dh_dt_initial(t, h):
    return ((t**(0.5)-25*h)/1000)
def dh_dt_final(t, h):
    return ((t**(0.5)-25*h-4)/1000)

t=0
h=0

tf=300
step_size=0.1
steps=int((tf-t)/step_size)

T=[t]
H=[h]

for step in range(steps):
    slope = dh_dt_initial(t, h)
    h += slope*step_size
    t += step_size
    H.append(h*100)
    T.append(t)

print(f"At t = 5 mins, h = {h*100:.4f} cm")

tf=600
step_size=0.1
steps=int((tf-300)/step_size)

for step in range(steps):
    slope = dh_dt_final(t, h)
    h += slope*step_size
    t += step_size
    H.append(h*100)
    T.append(t)

print(f"At t = 10 mins, h = {h*100:.4f} cm")

plt.plot(T,H)
plt.xlabel("Time (s)")
plt.ylabel("Height (cm)")
plt.grid()
plt.show()
import matplotlib.pyplot as plt
import numpy as np

k1 = 0.001
k2 = 0.1


def system(t, A, B, C):
    dA_dt = k2 * C - k1 * A * B
    dB_dt = k2 * C - k1 * A * B
    dC_dt = 2 * k1 * A * B - 2 * k2 * C
    return np.array([dA_dt, dB_dt, dC_dt])


# Initial conditions
t = 0
A = 100
B = 200
C = 0
h = 0.1  # step size
t_target = 10

steps = int((t_target - t) / h)
state = np.array([A, B, C])  # System state vector for coupled ODEs
print(f"Initial conditions: t = {t}, A = {A}, B = {B}, C = {C}")

# rk4 method setup
t_list = [t]
A_list = [A]
B_list = [B]
C_list = [C]

# Calculate using RK4 Method
for step in range(steps):
    # NOTE: The '*' operator unpacks the state array [A, B, C] into 3 separate arguments
    # so that system(t, *state) is equivalent to system(t, state[0], state[1], state[2]).
    m1 = system(t, *state)
    m2 = system(t + (h / 2), *(state + (h / 2) * m1))
    m3 = system(t + (h / 2), *(state + (h / 2) * m2))
    m4 = system(t + h, *(state + h * m3))

    avg_slope = (m1 + 2 * m2 + 2 * m3 + m4) / 6

    state = state + h * avg_slope
    t = t + h

    t_list.append(t)
    A_list.append(state[0])
    B_list.append(state[1])
    C_list.append(state[2])

print(f"RK4 final value: t = {t:.2f}, A = {state[0]:.2f}, B = {state[1]:.2f}, C = {state[2]:.2f}")

# Plotting
plt.figure(figsize=(10, 6))

plt.plot(t_list, A_list, label="Species A", color="blue")
plt.plot(t_list, B_list, label="Species B", color="green")
plt.plot(t_list, C_list, label="Species C", color="red")

plt.title("Reaction Kinetics (RK4 Method)")
plt.xlabel("t")
plt.ylabel("Concentration")
plt.legend()
plt.grid(True)
plt.show()
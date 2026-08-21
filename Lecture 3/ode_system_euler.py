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
h = 0.01  # Step size
t_target = 10

steps = int((t_target - t) / h)
state = np.array([A, B, C])  # System state vector for coupled ODEs
print(f"Initial conditions: t = {t}, A = {A}, B = {B}, C = {C}")

# Euler's method setup
t_list = [t]
A_list = [A]
B_list = [B]
C_list = [C]

# Calculate using Euler's Method
for step in range(steps):
    slopes = system(t, state[0], state[1], state[2])
    state = state + h * slopes
    t = t + h
    t_list.append(t)
    A_list.append(state[0])
    B_list.append(state[1])
    C_list.append(state[2])

print(f"Euler's method final value: t = {t:.2f}, A = {state[0]:.4f}, B = {state[1]:.4f}, C = {state[2]:.4f}")

# Plotting both curves
plt.figure(figsize=(10, 6))
plt.plot(t_list, A_list, label="Species A", color="blue")
plt.plot(t_list, B_list, label="Species B", color="green")
plt.plot(t_list, C_list, label="Species C", color="red")

plt.title("Reaction Kinetics Concentration vs Time (Euler Method)")
plt.xlabel("t")
plt.ylabel("Concentration")
plt.legend()
plt.grid(True)
plt.show()
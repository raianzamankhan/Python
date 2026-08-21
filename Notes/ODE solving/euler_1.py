import numpy as np
import matplotlib.pyplot as plt

def dy_dx(x,y):
    return 2*x

#initial conditions

x=1
y=1

h=0.1 #step size

x_target = 100

steps = int((x_target - x)/h)
print(f"The initial value of x = {x}, y = {y}")

# eulers method
x_list = [x]
y_list = [y]

for step in range(steps):
    slope = dy_dx(x,y)
    y = y + h*slope
    x = x+h
    x_list.append(x)
    y_list.append(y)
    print(f"Step {step+1}: x = {x:.2f}, y = {y:.2f}")

print(f"The final value of x = {x:.2f}, y = {y:.2f}")

plt.plot(x_list,y_list)
plt.show()
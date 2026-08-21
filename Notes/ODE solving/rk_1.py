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

# rk4 method
x_list = [x]
y_list = [y]

for step in range(steps):
    k1=dy_dx(x,y)
    k2=dy_dx(x+(h/2),y+(h/2)*k1)
    k3=dy_dx(x+(h/2),y+(h/2)*k2)
    k4=dy_dx(x+h,y+h*k3)
    avg_slope = ((k1+2*k2+2*k3+k4)/6)
    y = y + h*avg_slope
    x = x+h
    x_list.append(x)
    y_list.append(y)
    print(f"Step {step+1}: x = {x:.2f}, y = {y:.2f}")

print(f"The final value of x = {x:.2f}, y = {y:.2f}")

plt.plot(x_list,y_list)
plt.show()
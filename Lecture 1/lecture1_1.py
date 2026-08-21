import numpy as np
import matplotlib.pyplot as plt

# Define coefficient matrix A (3x3) and constants vector b (1x3)
A = np.array([[5, 4, 9], [2, 1, 4], [2, 5, 4]])
print(A)

b = np.array([95, 32, 61])
print(b)

# Calculate the determinant of matrix A
# np.linalg provides linear algebra tools: det() [determinant], inv() [inverse], solve() [Ax=b solver]

det_A = np.linalg.det(A)


# Check if matrix A is non-singular (invertible)
if det_A != 0:
    # Compute inverse matrix (A⁻¹)
    A_inv = np.linalg.inv(A)

    # Solve Ax = b via matrix multiplication: x = A⁻¹ * b
    # Note: '@' is Python's matrix multiplication operator (performs dot product, unlike '*' which is element-wise)
    x = A_inv @ b
    print("Solution is =", x)

    # plt.plot(x, y) plots x on the X-axis and y on the Y-axis (here: x -> X-axis, b -> Y-axis)
    plt.plot(x, b)
    plt.show()  # Displays plot (NB: Not needed in Google Colab)
else:
    print("No unique solution")  # Matrix is singular (determinant = 0)

# Alternative (Best Practice):
# x = np.linalg.solve(A, b) # Directly solves Ax = b faster and with better numerical stability
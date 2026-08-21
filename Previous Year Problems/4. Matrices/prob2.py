import numpy as np

# --- 1. DEFINE COEFFICIENT MATRIX A AND CONSTANTS VECTOR B ---
A = np.array([[3, 2, -1], [-1, 3, 2], [1, -1, -1]])
print("Matrix A:\n", A)

b = np.array([10, 5, -1])
print("\nVector b:\n", b)

# --- 2. CALCULATE THE DETERMINANT OF MATRIX A ---
# np.linalg.det() computes the determinant to test for invertibility
det_A = np.linalg.det(A)
print(f"\nDeterminant of A: {det_A:.2f}")

# --- 3. CHECK IF MATRIX A IS NON-SINGULAR AND SOLVE ---
if det_A != 0:
    # Compute inverse matrix (A⁻¹)
    A_inv = np.linalg.inv(A)

    # Solve Ax = b via matrix multiplication: x = A⁻¹ * b
    # '@' performs matrix multiplication (dot product)
    x = A_inv @ b
    print("\nSolution is =", x)

else:
    print("\nNo unique solution")  # Matrix is singular (determinant = 0)
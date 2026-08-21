import numpy as np

# --- Matrix Creation ---
A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]])
B = np.array([[1, 1], [1, 1], [1, 1]])

# --- a) Access value inside row 2 and column 2 of Matrix A ---
# Note: Python uses 0-based indexing, so row 2, column 2 is index [1, 1]
val_a = A[1, 1]
print(f"\nRow 2, Col 2 of Matrix A is: {val_a}")

# --- b) Access the second column of Matrix B ---
# ':' in the row position means "select ALL rows"
# '1' in the column position means "select index 1" (2nd column)
val_b = B[:, 1]  # Extracts the entire 2nd column
print(f"\nSecond column of Matrix B is: {val_b}")

# --- c) Size, maximum value, and minimum value of Matrix A ---
size_A = A.shape
max_A = np.max(A)
min_A = np.min(A)
print(f"\nSize of A Matrix is: {size_A}, Max Value: {max_A}, Min Value: {min_A}")

# --- d) Add, subtract, multiply, and divide Matrix A and B ---
# Matrix Multiplication: (3x3) @ (3x2) -> resulting shape (3, 2)
A_times_B = A @ B

# For element-wise operations (+, -, *, /), we pad B with a column of zeros
# ((0,0) rows top/bottom, (0,1) columns left/right) so B becomes 3x3
B_padded = np.pad(B, ((0, 0), (0, 1)))

A_plus_B = A + B_padded
A_minus_B = A - B_padded
A_elem_mult = A * B_padded  # Element-wise multiplication

# Suppress runtime warning for division by 0 in the padded column
with np.errstate(divide='ignore'):
    A_div_B = A / B_padded

print("\nMatrix Multiplication (A @ B):\n", A_times_B)
print("\nElement-wise Addition (A + B):\n", A_plus_B)
print("\nElement-wise Subtraction (A - B):\n", A_minus_B)
print("\nElement-wise Multiplication (A * B):\n", A_elem_mult)
print("\nElement-wise Division (A / B):\n", A_div_B)

# --- e) Flip Matrix A Left-Right and Matrix B Up-Down ---
A_flipped_lr = np.fliplr(A)
B_flipped_ud = np.flipud(B)

print("\nMatrix A flipped Left-Right:\n", A_flipped_lr)
print("\nMatrix B flipped Up-Down:\n", B_flipped_ud)
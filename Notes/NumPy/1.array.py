import numpy as np

# 1. Python List Multiplication (Sequence Repetition)
my_list = [1, 2, 3, 4]
print(my_list * 2) 
# Output: [1, 2, 3, 4, 1, 2, 3, 4]
# Note: Standard Python lists duplicate/repeat their contents when multiplied.

# 2. NumPy Array Multiplication (Vectorized Arithmetic)
array = np.array([1, 2, 3, 4])
print(array * 2) 
# Output: [2 4 6 8]
# Note: NumPy arrays perform element-wise math, multiplying each individual item.

# 3. 0-Dimensional Array (Scalar)
array = np.array("A")
# Note: A single value with 0 opening brackets '[' is a 0D scalar (shape: ()).
print(array.ndim) 
# Output: 0
print(array.shape)
# Output: ()
print(array.size)
# Output: 1

# 4. 1-Dimensional Array (Vector)
array = np.array(["A", "B", "C"])
# Note: A flat list with 1 opening bracket '[' forms a 1D vector (shape: (3,)).
print(array.ndim) 
# Output: 1
print(array.shape)
# Output: (3,)
print(array.size)
# Output: 3

# NOTE: Every sub-list at the same level MUST have the exact same number of elements!

# 5. 2-Dimensional Array (Matrix)
array = np.array([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])
# Note: A grid formed by 2 opening brackets '[[' (shape: (3, 3)).
print(array.ndim) 
# Output: 2
print(array.shape)
# Output: (3, 3)
print(array.size)
# Output: 9

# 6. 3-Dimensional Array (Tensor / Stack of Matrices)
array = np.array([
    [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
    [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]
])
# Note: A 3D tensor formed by 3 opening brackets '[[[' (shape: (3, 3, 3)).
print(array.ndim)
# Output: 3
print(array.shape)
# Output: (3, 3, 3)
print(array.size)
# Output: 27
import numpy as np

array = np.array([
    [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]],
    [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]],
    [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]
])

# --- Multidimensional Indexing ---

print(array[0][0][0])  # Standard Python chain indexing
# Output: A

print(array[0, 0, 0])  # NumPy tuple indexing (faster & cleaner)
# Output: A

# Indexing letters to form "CAT":
# array[0, 0, 2] -> "C" (Matrix 0, Row 0, Col 2)
# array[0, 0, 0] -> "A" (Matrix 0, Row 0, Col 0)
# array[2, 0, 1] -> "T" (Matrix 2, Row 0, Col 1)
word = array[0, 0, 2] + array[0, 0, 0] + array[2, 0, 1]

print(word) 
# Output: CAT
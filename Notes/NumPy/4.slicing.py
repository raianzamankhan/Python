import numpy as np

# Base 2D Array (4x4 Matrix)
array = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 11, 12],
    [13, 14, 15, 16]
])

# 2D Slicing Syntax: array[row_slice, col_slice]
# Slicing Syntax: [start:stop:step] (stop is exclusive)

# ==================== ROW SLICING ====================

# 1. First row (Single Row Indexing)
print(array[0])
# Output: [1 2 3 4]

# 2. First 2 rows (Rows 0 and 1)
print(array[:2])
# Output:
# [[1 2 3 4]
#  [5 6 7 8]]

# 3. 2nd row to last row (Row index 1 to end)
print(array[1:])
# Output:
# [[ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

# 4. Jumping 1 row (Every 2nd row: Row 0, then Row 2)
print(array[::2])
# Output:
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# 5. Reverse rows (Flips row order upside down)
print(array[::-1])
# Output:
# [[13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# 6. Jumping 1 row in reverse order (Row 3, then Row 1)
print(array[::-2])
# Output:
# [[13 14 15 16]
#  [ 5  6  7  8]]

# ==================== COLUMN SLICING ====================

# 1. First column (All rows ':', Column index 0)
print(array[:, 0])
# Output: [ 1  5  9 13]

# 2. First 2 columns (All rows ':', Columns 0 and 1)
print(array[:, :2])
# Output:
# [[ 1  2]
#  [ 5  6]
#  [ 9 10]
#  [13 14]]

# 3. 2nd column to last column (All rows ':', Column index 1 to end)
print(array[:, 1:])
# Output:
# [[ 2  3  4]
#  [ 6  7  8]
#  [10 11 12]
#  [14 15 16]]

# 4. Jumping 1 column (Every 2nd column: Col 0, then Col 2)
print(array[:, ::2])
# Output:
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

# 5. Reverse columns (Flips column order left-to-right)
print(array[:, ::-1])
# Output:
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]
#  [16 15 14 13]]

# 6. Reverse columns jumping 1 (Col 3, then Col 1)
print(array[:, ::-2])
# Output:
# [[ 4  2]
#  [ 8  6]
#  [12 10]
#  [16 14]]

# ==================== COMBINED (ROW + COLUMN) SLICING ====================

# 1. First 2 rows and First 2 columns (Top-Left 2x2 Sub-matrix)
print(array[:2, :2])
# Output:
# [[1 2]
#  [5 6]]

# 2. Last 2 rows and Last 2 columns (Bottom-Right 2x2 Sub-matrix)
print(array[2:, 2:])
# Output:
# [[11 12]
#  [15 16]]

# 3. Inner 2x2 block (Rows 1-2, Columns 1-2)
print(array[1:3, 1:3])
# Output:
# [[ 6  7]
#  [10 11]]

# 4. Step through both rows and columns (Every 2nd row & column)
print(array[::2, ::2])
# Output:
# [[ 1  3]
#  [ 9 11]]

# 5. Fully reverse both rows and columns (Rotates matrix 180 degrees)
print(array[::-1, ::-1])
# Output:
# [[16 15 14 13]
#  [12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]
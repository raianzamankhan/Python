import numpy as np

# ==========================================
# 1. np.arange(start, stop, step)
# Generates numbers within a given interval with a fixed STEP SIZE.
# Range is [start, stop) -> Includes start, EXCLUDES stop.
# ==========================================

arr1 = np.arange(0, 10, 2)
print(arr1)
# Output: [0 2 4 6 8]

# Default start is 0, default step is 1:
arr2 = np.arange(5)
print(arr2)
# Output: [0 1 2 3 4]

# Supports floating-point step sizes:
arr3 = np.arange(0, 1, 0.2)
print(arr3)
# Output: [0.  0.2 0.4 0.6 0.8]

# Step larger than interval (step > stop - start):
arr4 = np.arange(0, 10, 50)
print(arr4)
# Output: [0]


# ==========================================
# 2. np.linspace(start, stop, num)
# Generates a specified NUMBER of evenly spaced values over an interval.
# Range is [start, stop] -> INCLUDES both start AND stop by default!
# ==========================================

arr5 = np.linspace(0, 1, 5)
print(arr5)
# Output: [0.   0.25 0.5  0.75 1.  ]

# Default num is 50 if omitted:
arr6 = np.linspace(0, 10)
print(arr6)
# Output: [0. 0.20408163 ... 10.]

# Supports floating-point intervals:
arr7 = np.linspace(0.1, 0.9, 5)
print(arr7)
# Output: [0.1 0.3 0.5 0.7 0.9]

# Optional: Exclude the stop value using endpoint=False
arr8 = np.linspace(0, 10, 5, endpoint=False)
print(arr8)
# Output: [0. 2. 4. 6. 8.]
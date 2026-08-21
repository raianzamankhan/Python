N = int(input("Enter a positive integer N: "))

# ----------------------------------------------------
# SERIES 1: 0 + 1 + 2 + ... + N
# ----------------------------------------------------

sum_for = 0
# i starts at 0 (the first term of the series).
# Note: The step size (1) is omitted here because 1 is the default step in range().
for i in range(0, N + 1):
    sum_for += i

print(f"For Loop Series 1: {sum_for}")

sum_while = 0
i = 0  # i is the first term of the series
while i <= N:
    sum_while += i  
    i += 1  

print(f"While Loop Series 1: {sum_while}")
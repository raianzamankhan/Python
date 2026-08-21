N = int(input("Enter a positive integer N: "))

# ----------------------------------------------------
# SERIES 6: 1 + 3 + 9 + 27 + ... + N
# ----------------------------------------------------

# 1. FOR LOOP
sum_for = 0
i = 1  # i starts at 1 (the first term of the series)

# Note: Python's range(start, stop, step) can only ADD or SUBTRACT a fixed step.
# It cannot multiply (e.g. step by *3). Therefore, we use range(N + 1) purely
# as a step counter and manually multiply 'i' inside the loop body instead.

for x in range(N + 1):
    # Stop the loop once the current term exceeds N
    if i > N:
        break
    sum_for += i
    i *= 3  # Multiply by 3 to generate the next term in the series

print(f"For Loop Series 3: {sum_for}")

# 2. WHILE LOOP
sum_while = 0
i = 1  # i is the first term of the series

while i <= N:
    sum_while += i
    i *= 3  # Next term is multiplied by 3

print(f"While Loop Series 3: {sum_while}")
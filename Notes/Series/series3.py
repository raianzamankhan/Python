N = int(input("Enter a positive integer N: "))

# ----------------------------------------------------
# SERIES 3: 1^2 + 2^2 + 3^2 + ... + N^2
# ----------------------------------------------------

# 1. FOR LOOP
sum_for = 0
for i in range(1, N + 1):
    sum_for += i**2

print(f"For Loop Series 4: {sum_for}")

# 2. WHILE LOOP
sum_while = 0
i = 1  # i starts at 1 (the base of the first term)
while i <= N:
    sum_while += i**2
    i += 1

print(f"While Loop Series 4: {sum_while}")
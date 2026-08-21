N = int(input("Enter a positive integer N: "))

# ----------------------------------------------------
# SERIES 2: 100 + 98 + 96 + ... + N
# ----------------------------------------------------

sum_for = 0
# i starts at 100 (the first term of the series).
# range(100, N - 1, -2):
# - Stops at N - 1 so that N itself is included.
# - Step is -2 because the series decreases by 2 each time.
for i in range(100, N - 1, -2):
    sum_for += i  

print(f"For Loop Series 2: {sum_for}")

sum_while = 0
i = 100  # i is the first term of the series
while i >= N:
    sum_while += i  
    i -= 2  

print(f"While Loop Series 2: {sum_while}")
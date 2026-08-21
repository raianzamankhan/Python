numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        continue  # Skips 30
    if num == 50:
        break     # Stops loop completely at 50
    print(num)

# Output:
# 10
# 20
# 40
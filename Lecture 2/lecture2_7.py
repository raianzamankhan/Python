for i in range(1, 4):         # Outer loop: controls rows (i = 1, 2, 3)
    for j in range(1, 4):     # Inner loop: controls columns (j = 1, 2, 3)
        print(i * j, end=" ") # Prints product on same line with a space
    print()                   # Moves cursor to next line after inner loop finishes
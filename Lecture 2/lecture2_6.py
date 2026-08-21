for i in range(1, 4):
    # end=" " overrides the default newline (\n) and puts a space after each number
    print(i, end=" ")
# Output: 1 2 3 

print() # MOVES CURSOR TO THE NEXT LINE!

for i in range(1, 4):
    # end=", " puts a comma and space after each printed item on the same line
    print(i, end=", ")
# Output: 1, 2, 3,

print() # MOVES CURSOR TO THE NEXT LINE!

for i in range(1, 4):
    if i == 3:
        print(i)          # Last item: prints 3 with a normal newline
    else:
        print(i, end=", ") # Prints '1, ' and '2, '
# Output: 1, 2, 3
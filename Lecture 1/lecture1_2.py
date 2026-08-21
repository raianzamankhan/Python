a = 5
b = 7
c = a + b
print('The sum of', a, 'and', b, 'is =', c)
print("The sum of " + str(a) + " and " + str(b) + " is = " + str(c))
print(f"The sum of {a} and {b} is = {c}")

d = input("Enter the first number: ")
e = input("Enter the second number: ")
#An input is always stored as a string
f = int(d) + int(e)
print(f"The sum of {d} and {e} is = {f}")
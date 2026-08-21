win = int(input("Matches Won: "))
loss = int(input("Matches Lost: "))
draw = int(input("Matches Drew: "))

point = win*3 + draw

print(f"Number of matches won {win}, lost {loss}, drew {draw} and the final point is {point}")

if point>=5:
  print("Qualified for the Round of 32")
else:
  print("They are eliminated")
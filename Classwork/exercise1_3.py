Items = ["Rice", "Oil", "Sugar", "Milk", "Eggs", "Bread", "Butter"]
Price = [110, 180, 75, 65, 120, 55, 210]
Quantity = [2, 1, 3, 4, 2, 2, 1]

Cost = []        # Initialized as an empty list to store computed costs
Total_Cost = 0   # Initialized to zero to accumulate the running total cost

# 1. Calculate costs and total
for i in range(0, 7):
    c = Price[i] * Quantity[i]
    Cost.append(c)
    Total_Cost += c

# 2. Bubble Sort While (Sorting all parallel lists by Cost in ascending order)
i = 0
n = len(Cost)
while i < (n - 1):
    j = 0
    while j < (n - 1 - i):
        # COMPARE j with j+1 (adjacent elements)
        if Cost[j] < Cost[j + 1]:
            Cost[j], Cost[j + 1] = Cost[j + 1], Cost[j]
            Quantity[j], Quantity[j + 1] = Quantity[j + 1], Quantity[j]
            Price[j], Price[j + 1] = Price[j + 1], Price[j]
            Items[j], Items[j + 1] = Items[j + 1], Items[j]
        j += 1
    i += 1

# --- HEADER ---
print("Items", "Price", "Qty", "Cost", sep="\t")
print("-" * 30)

# 3. Print sorted output
for i in range(0, 7):
    print(Items[i], Price[i], Quantity[i], Cost[i], sep="\t")

# --- FOOTER ---
print("-" * 30)
print(f"Total Cost:\t\t{Total_Cost}")

# --- HIGHEST & LOWEST COST ITEMS ---
print(f"Highest Cost Item:\t{Items[0]} ({Cost[0]})")
print(f"Lowest Cost Item:\t{Items[-1]} ({Cost[-1]})")
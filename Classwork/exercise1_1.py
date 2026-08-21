Items = ["Rice", "Oil", "Sugar", "Milk", "Eggs", "Bread", "Butter"]
Price = [110, 180, 75, 65, 120, 55, 210]
Quantity = [2, 1, 3, 4, 2, 2, 1]

Cost = []         # Initialized as an empty list to store computed costs
Total_Cost = 0   # Initialized to zero to accumulate the running total cost

# --- HEADER ---
print("Items", "Price", "Qty", "Cost", sep="\t")
print("-" * 30)

for i in range(0, 7):
    # 1. Calculate cost for the current item
    c = Price[i] * Quantity[i]
    
    # 2. Append cost to list
    Cost.append(c)
    
    # 3. Add current item's cost to total
    Total_Cost += c
    
    # 4. Print current row aligned under headers
    print(Items[i], Price[i], Quantity[i], Cost[i], sep="\t")

# --- FOOTER ---
print("-" * 30)
print(f"Total Cost:\t\t{Total_Cost}")
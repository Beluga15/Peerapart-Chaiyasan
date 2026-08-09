#Assignment 2.1
scores = []

for i in range(5):
    score = int(input("Enter your score :"))
    scores.append(score)
    
for i in range(5):
    if scores[i] >=50: 
      print(f"Student {i+1}: {scores} -> Pass")
    else:
      print(f"Student {i+1}: {scores} -> Not pass")

#Assignment 2.2
prices = []

for i in range(6):
    price = int(input("Enter prices of 6 item:"))
    prices.append(price)
    
budget = int(input("\nEnter total budget:"))

total= 0
bought_items = []
for i in range(6):
    price = prices [i] 
    
    if total + price <= budget:
        print(f"Item {i+1} = {price} ->Buy")
        total += price
        bought_items.append(price)
        print(f"Current total = {total}")
    else:
        print(f"\nItem {i+1} = {price} -> Cannot buy")
        print(f"Current total = {total}")

print(f"\nBought items: {bought_items}")
print(f"Total spent: {total}")
print(f"Remaining budget: {budget - total}")
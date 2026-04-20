# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

# Initialize the ordered dictionary
inventory = OrderedDict()

# Read the number of items
n = int(input())

for _ in range(n):
    # Split from the right once to separate name and price
    data = input().rsplit(' ', 1)
    item_name = data[0]
    net_price = int(data[1])
    
    # Update the total price for the item
    if item_name in inventory:
        inventory[item_name] += net_price
    else:
        inventory[item_name] = net_price

# Print the results in order of first occurrence
for item, total in inventory.items():
    print(f"{item} {total}")

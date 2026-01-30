items = ["Greek Yogurt", "Eggs", "Milk", "Chicken", "Onion"]

new_item = input("Enter Grocery Item You Like to Add: ").strip().title()

if new_item not in items:
    items.append(new_item)
else:
    print("Item already exists")

print("Updated Grocery List:")
for grocery in items:
    print(grocery)

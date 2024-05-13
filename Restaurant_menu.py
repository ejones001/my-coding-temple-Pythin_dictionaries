# Initial restaurant menu
restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# 1.
restaurant_menu["Beverages"] = {"Water": 1.50, "Soda": 2.00}

# 2.
restaurant_menu["Main Course"]["Steak"] = 17.99

# Task 3: Remove "Bruschetta" from "Starters"
del restaurant_menu["Starters"]["Bruschetta"]

# 3.
print("Updated Restaurant Menu:")
for category, items in restaurant_menu.items():
    print(f"{category}:")
    for item, price in items.items():
        print(f"\t{item}: ${price:.2f}")

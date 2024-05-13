import copy

# Given sales data
weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

# Create a deep copy of weekly_sales
copied_weekly_sales = copy.deepcopy(weekly_sales)

# Update the sales figure for "Electronics" in "Week 2" in the copied data
copied_weekly_sales["Week 2"]["Electronics"] = 18000

# Print the updated copied data
print("Updated Sales Data (Deep Copy):")
print(copied_weekly_sales)

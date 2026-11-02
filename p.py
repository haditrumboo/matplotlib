import numpy as np

products = np.array([
    "Laptop", "Phone", "Tablet", "Monitor", "Keyboard",
    "Mouse", "Headphones", "Webcam", "Printer", "Speaker"
])

prices = np.array([
    75000, 30000, 20000, 15000, 2000,
    800, 5000, 3000, 12000, 4000
])

units_sold = np.array([
    12, 35, 20, 18, 60, 100, 45, 25, 10, 30
])

cost_per_unit = np.array([
    60000, 22000, 14000, 10000, 1000,
    300, 3000, 1800, 9000, 2500
])

revenue = prices * units_sold

print("PRODUCT REVENUE")
for i in range(len(products)):
    print(f"{products[i]}: ₹{revenue[i]}")


calculated_profit = (prices - cost_per_unit) * units_sold

print("\nPRODUCT PROFIT")
for i in range(len(products)):
    print(f"{products[i]}: ₹{calculated_profit[i]}")

highest_profit_index = np.argmax(calculated_profit)
lowest_profit_index = np.argmin(calculated_profit)

print("\nHighest profit product:", products[highest_profit_index])
print("Lowest profit product:", products[lowest_profit_index])
print("Total company profit: ₹", np.sum(calculated_profit))


profit_margin = ((prices - cost_per_unit) / prices) * 100

mask = (revenue > 100000) & (profit_margin > 30)

print("\nPRODUCTS WITH REVENUE > ₹100,000 AND PROFIT MARGIN > 30%")

for i in np.where(mask)[0]:
    print(
        f"{products[i]}: "
        f"Revenue = ₹{revenue[i]}, "
        f"Profit Margin = {profit_margin[i]:.2f}%"
    )
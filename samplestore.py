import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:/Users/Manish/Downloads/SampleSuperstore.csv"
df = pd.read_csv(file_path)

df = df.drop(columns=["Ship Mode", "Postal Code"])

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
average_order_value = df["Sales"].mean()
overall_profit_margin = (total_profit / total_sales) * 100

print(f"Total Sales: {total_sales:.2f}")
print(f"Total Profit: {total_profit:.2f}")
print(f"Average Order Value: {average_order_value:.2f}")
print(f"Overall Profit Margin: {overall_profit_margin:.2f}%")

sales_by_region = df.groupby("Region")["Sales"].sum()
profit_by_region = df.groupby("Region")["Profit"].sum()

sales_by_region.plot(kind="bar", title="Sales by Region", ylabel="Sales")
plt.show()

profit_by_region.plot(kind="bar", title="Profit by Region", ylabel="Profit")
plt.show()

sales_by_category = df.groupby("Category")["Sales"].sum()
profit_by_category = df.groupby("Category")["Profit"].sum()

sales_by_category.plot(kind="bar", title="Sales by Category", ylabel="Sales")
plt.show()

profit_by_category.plot(kind="bar", title="Profit by Category", ylabel="Profit")
plt.show()

sales_by_subcategory = df.groupby("Sub-Category")["Sales"].sum()
profit_by_subcategory = df.groupby("Sub-Category")["Profit"].sum()
quantity_by_subcategory = df.groupby("Sub-Category")["Quantity"].sum()

sales_by_subcategory.plot(
    kind="pie",
    title="Sales by Sub-Category",
    autopct="%1.1f%%",
    figsize=(8, 8)
)
plt.ylabel("")
plt.show()

profit_by_subcategory.sort_values().plot(
    kind="bar",
    title="Profit by Sub-Category",
    ylabel="Profit"
)
plt.show()

sales_by_discount = df.groupby("Discount")["Sales"].sum().round()
profit_by_discount = df.groupby("Discount")["Profit"].sum().round()

sales_contribution_region = (sales_by_region / total_sales) * 100

profit_margin_region = (profit_by_region / sales_by_region) * 100
print("\nProfit Margin by Region:")
print(profit_margin_region.round(2))

category_sales_contribution = (sales_by_category / total_sales) * 100

print("\nCategory Sales Contribution (%):")
print(category_sales_contribution.sort_values().round(2))

best_products_by_region = df.loc[
    df.groupby("Region")["Sales"].idxmax(),
    ["Region", "Sub-Category", "Sales", "Profit", "Quantity"]
]

print("\nBest Performing Products by Region:")
print(best_products_by_region)

high_sales_regions = sales_by_region[sales_by_region > sales_by_region.mean()]
low_profit_regions = profit_by_region[profit_by_region < profit_by_region.mean()]

print("\nHigh Sales Regions:")
print(high_sales_regions)

print("\nLow Profit Regions:")
print(low_profit_regions)

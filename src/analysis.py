import pandas as pd

orders = pd.read_csv("Data/processed/orders.csv")
order_items = pd.read_csv("Data/processed/order_items.csv")
order_payments = pd.read_csv("Data/processed/order_payments.csv")
order_reviews = pd.read_csv("Data/processed/order_reviews.csv")
products = pd.read_csv("Data/processed/products.csv")
customer = pd.read_csv("Data/processed/customer.csv")

#Total Revenue
total_revenue = order_payments["payment_value"].sum()
print("Total_revenue:", round(total_revenue,2))

#Total_orders
total_orders = orders["order_id"].nunique()
print("Total orders:", total_orders)

#Average order value
average_order_value = total_revenue/total_orders
print("Average order value:",round(average_order_value,2))

#Average review score
average_review_score = order_reviews["review_score"].mean()
print("Average Review Score:",round(average_review_score,2))

#Average delivery time in days 
orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])
orders["order_delivered_customer_date"] = pd.to_datetime(orders["order_delivered_customer_date"])

delivery_days = (orders["order_delivered_customer_date"] -orders["order_purchase_timestamp"]).dt.days
average_delivery_days = delivery_days.mean()
print("Average Delivery Time:", round(average_delivery_days, 2), "days")

# Average freight value
average_freight_value = order_items["freight_value"].mean()

print("Average Freight Value:", round(average_freight_value, 2))


# Monthly revenue
orders["month"] = orders["order_purchase_timestamp"].dt.to_period("M")

monthly_revenue = (
    order_payments
    .merge(orders[["order_id", "month"]], on="order_id")
    .groupby("month")["payment_value"]
    .sum()
)

print("\nMonthly Revenue:")
print(monthly_revenue)


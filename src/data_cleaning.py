import pandas as pd

customers = pd.read_csv("Data/raw/olist_customers_dataset.csv")
gelocation = pd.read_csv("Data/raw/olist_geolocation_dataset.csv")
order_items = pd.read_csv("Data/raw/olist_order_items_dataset.csv")
order_payments = pd.read_csv("Data/raw/olist_order_payments_dataset.csv")
order_reviews = pd.read_csv("Data/raw/olist_order_reviews_dataset.csv")
orders = pd.read_csv("Data/raw/olist_orders_dataset.csv")
products = pd.read_csv("Data/raw/olist_products_dataset.csv")
sellers = pd.read_csv("Data/raw/olist_sellers_dataset.csv")
product_category_name_translation = pd.read_csv("Data/raw/product_category_name_translation.csv")

print("All Dataset Loaded Succesfully!")


print("\nMissing values before cleaning")

for name, df in {
    "customers": customers,
    "Geolocation": gelocation,
    "Order Items": order_items,
    "Order Payments": order_payments,
    "Order Reviws": order_reviews,
    "Orders": orders,
    "Products": products,
    "Sellers": sellers,
    "Product Category Name Translation": product_category_name_translation
}.items():

    print(f"\n{name}")
    print(df.isnull().sum()[lambda x:x >0])


print("\nOrders - Missing Date by Order status:")

print(
    orders.groupby("order_status")[
        [
            "order_approved_at",
            "order_delivered_carrier_date",
            "order_delivered_customer_date"
        ]
    ].apply(lambda x: x.isnull().sum())
)

print(
    orders[
        (orders["order_status"] == "delivered")&
        (orders["order_approved_at"].isnull())
    ]
)

print("\nProducts- Missing Category Rows:")
print(
    products[products["product_category_name"].isnull()]
    .head(10)
)

print("\nProduct- Missing physical date")
print(
    products[
        products[
            [
                "product_weight_g",
                "product_length_cm",
                "product_height_cm",
                "product_width_cm"
            ]
        ].isnull().any(axis=1)
    ]
)

print("\nDuplicate Rows:")

datasets = {
    "customers": customers,
    "Geolocation": gelocation,
    "Order Items": order_items,
    "Order Payments": order_payments,
    "Order Reviws": order_reviews,
    "Orders": orders,
    "Products": products,
    "Sellers": sellers,
    "Product Category Name Translation": product_category_name_translation

    }
for name,df in datasets.items():
    print(f"{name}:{df.duplicated().sum()}")

print("\nGelocation Duplicatre check:")

print("Full row Duplication:", gelocation.duplicated().sum())
print("Duplicate Zip codes:", gelocation["geolocation_zip_code_prefix"].duplicated().sum())

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_carrier_date",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for column in date_columns:
    orders[column] = pd.to_datetime(orders[column])

print("\nDate column Convert Suesccesfully!")
print(orders[date_columns].dtypes)

order_items["shipping_limit_date"] = pd.to_datetime(order_items["shipping_limit_date"])
print(order_items["shipping_limit_date"].dtype)

review_date_column = [
    "review_creation_date",
    "review_answer_timestamp"
]

for column in review_date_column:
    order_reviews[column] = pd.to_datetime(order_reviews[column])

print("\nreview date column convert Succesfully.")
print(order_reviews[review_date_column].dtypes)

products.rename(columns={
    "product_name_lenght": "product_name_length",
    "product_description_lenght": "product_description_length"
}, inplace=True)

print("\nProduct column rename sucessfully!")
print(products.columns.tolist())

print("\nNumeric column Data types:")

print(products.dtypes)
print(order_items.dtypes)
print(order_payments.dtypes)
print(order_reviews.dtypes)


customers.to_csv("Data/processed/customer.csv", index=False)
gelocation.to_csv("Data/processed/geolocation.csv", index=False)
order_items.to_csv("Data/processed/order_items.csv", index=False)
order_payments.to_csv("Data/processed/order_payments.csv", index=False)
order_reviews.to_csv("Data/processed/order_reviews.csv", index=False)
orders.to_csv("Data/processed/orders.csv", index=False)
products.to_csv("Data/processed/products.csv", index=False)
sellers.to_csv("Data/processed/sellers.csv", index=False)
product_category_name_translation.to_csv("Data/processed/product_category_name_translation.csv", index=False)

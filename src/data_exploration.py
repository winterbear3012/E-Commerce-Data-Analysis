import pandas as pd

#Load Datasets
customers = pd.read_csv("Data/raw/olist_customers_dataset.csv")
gelocation = pd.read_csv("Data/raw/olist_geolocation_dataset.csv")
order_items = pd.read_csv("Data/raw/olist_order_items_dataset.csv")
order_pyments = pd.read_csv("Data/raw/olist_order_payments_dataset.csv")
order_reviews = pd.read_csv("Data/raw/olist_order_reviews_dataset.csv")
orders = pd.read_csv("Data/raw/olist_orders_dataset.csv")
products = pd.read_csv("Data/raw/olist_products_dataset.csv")
sellers = pd.read_csv("Data/raw/olist_sellers_dataset.csv")
product_category_name_translation = pd.read_csv("Data/raw/product_category_name_translation.csv")

print("Dataset Loaded Succesfully!")

#Check number of rows
print("Nubers of rows:\n")

print("Customer:", len(customers))
print("Geolocation:", len(gelocation))
print("Order Items:", len(order_items))
print("Order Pyments:", len(order_pyments))
print("Order Reviews:", len(order_reviews))
print("Order:", len(orders))
print("Product:", len(products))
print("seller:", len(sellers))
print("Product category Name Translation:", len(product_category_name_translation))

#check columns
print("Columns:\n")

print("Coustomers:", customers.columns.tolist())
print("Gelocation:", gelocation.columns.tolist())
print("Order Items:", order_items.columns.tolist())
print("Order Payments:", order_pyments.columns.tolist())
print("Order Reviews:", order_reviews.columns.tolist())
print("Orders:", orders.columns.tolist())
print("Products:", products.columns.tolist())
print("Sellers:", sellers.columns.tolist())
print("Product Category Name Translation:", product_category_name_translation.columns.tolist())

#Check DataTypes
print("\nData Types:")

print("\nCustomers:")
print(customers.dtypes)

print("\nGeolocation:")
print(gelocation.dtypes)

print("\nOrder Items:")
print(order_items.dtypes)

print("\nOrder Payments:")
print(order_pyments.dtypes)

print("\nOrder Reviews:")
print(order_reviews.dtypes)

print("\nOrders:")
print(orders.dtypes)

print("\nProducts:")
print(products.dtypes)

print("\nSellers:")
print(sellers.dtypes)

print("\nProduct Category Name Translation:")
print(product_category_name_translation.dtypes)


#Check missing value
print("\nMissing Value:")

print("\nCustomer:")
print(customers.isnull().sum())

print("\nGeolocation:")
print(gelocation.isnull().sum())

print("\nOrder Items:")
print(order_items.isnull().sum())

print("\nOrder Payments:")
print(order_pyments.isnull().sum())

print("\nOrder Reviews:")
print(order_reviews.isnull().sum())

print("\nOrders:")
print(orders.isnull().sum())

print("\nProducts:")
print(products.isnull().sum())

print("\nSellers:")
print(sellers.isnull().sum())

print("\nProduct category Name Transaltion:")
print(product_category_name_translation.isnull().sum())

#Check Duplicate Rows
print("\nDuplicate Rows:")

print("Customers:", customers.duplicated().sum())
print("Gelolocation:", gelocation.duplicated().sum())
print("Order Items:", order_items.duplicated().sum())
print("Order Payments:", order_pyments.duplicated().sum())
print("Order Reviews:", order_reviews.duplicated().sum())
print("Orders:", orders.duplicated().sum())
print("Products:", products.duplicated().sum())
print("Sellers:", sellers.duplicated().sum())
print("Product Category Name Translation:", product_category_name_translation.duplicated().sum())

#Check Unique Value
print("\nUnique Value:")

print("Customer:")
print(customers.nunique())

print("Geolocaation:")
print(gelocation.nunique())

print("Order Items:")
print(order_items.nunique())

print("Order Paymnets:")
print(order_pyments.nunique())

print("Order Reviews:")
print(order_reviews.nunique())

print("Orders:")
print(orders.nunique())

print("Products:")
print(products.nunique())

print("Sellers:")
print(sellers.nunique())

print("Product Category Name Translation:")
print(product_category_name_translation.nunique())

#sample record
print("\nSample Records:")

print("Customers")
print(customers.head())

print("Geolocation")
print(gelocation.head())

print("Order Items")
print(order_items.head())

print("Order Payment")
print(order_pyments.head())

print("Order Reviews")
print(order_reviews.head())

print("Orders")
print(orders.head())

print("Products")
print(products.head())

print("Sellers")
print(sellers.head())

print("Product category Name Translation")
print(product_category_name_translation.head())


# 🌟 Exercise 2 : Advanced Data Manipulation and Analysis
# Instructions
# In this exercise, you will analyze data from a hypothetical online retail company to gain insights into sales trends and customer behavior. The data is represented as a list of dictionaries, where each dictionary contains information about a single purchase.

# sales_data = [
#     {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
#     {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
#     {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
#     {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
#     {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
#     {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
#     {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
# ]

# Tasks:
# Total Sales Calculation: Calculate the total sales for each product category (i.e., the total revenue generated from each type of product). Use a loop to iterate through the data and a dictionary to store the total sales for each product.

# Customer Spending Profile: Determine the total amount spent by each customer. Use a dictionary to maintain the sum of amounts each customer has spent.

# Sales Data Enhancement:
# Add a new field to each transaction called “total_price” that represents the total price for that transaction (quantity * price).
# Use a loop to modify the sales_data list with this new information.

# High-Value Transactions:
# Using list comprehension, create a list of all transactions where the total price is greater than $500.
# Sort this list by the total price in descending order.

# Customer Loyalty Identification:
# Identify any customer who has made more than one purchase, suggesting potential loyalty.
# Use a dictionary to count purchases per customer, then use a loop or comprehension to identify customers meeting the loyalty criterion.

# Bonus: Insights and Analysis:
# Calculate the average transaction value for each product category.
# Identify the most popular product based on the quantity sold.
# Provide insights into how these analyses could inform the company’s marketing strategies.


sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

def create_product_revenue_dict(sales_data: list) -> dict:
    product_revenue = dict()
    for customer in sales_data:
        if customer["product"] not in product_revenue:
            product_revenue[customer["product"]] = customer["price"] * customer["quantity"]
        else:
            product_revenue[customer["product"]] += customer["price"] * customer["quantity"]
    return product_revenue

def create_customer_spending_dict(sales_data: list) -> dict:
    customer_spending = dict()
    for customer in sales_data:
        if customer["customer_id"] not in customer_spending:
            customer_spending[customer["customer_id"]] = customer["price"] * customer["quantity"]
        else:
            customer_spending[customer["customer_id"]] += customer["price"] * customer["quantity"]
    return customer_spending

def add_total_price(sales_data: list) -> None:
    for customer in sales_data:
        customer["total_price"] = customer["price"] * customer["quantity"]

def create_customer_purchase_quantity_dict(sales_data: list) -> dict:
    quantity_per_customer = dict()
    for transaction in sales_data:
        if transaction["customer_id"] not in quantity_per_customer:
            quantity_per_customer[transaction["customer_id"]] = transaction["quantity"]
        else:
            quantity_per_customer[transaction["customer_id"]] += transaction["quantity"]
    return quantity_per_customer

def create_loyalty_dict(sales_data: list) -> dict:
    loyal_customers_dict = dict()
    quantity_per_customer = create_customer_purchase_quantity_dict(sales_data)
    print(quantity_per_customer)
    for customer in quantity_per_customer:
        if quantity_per_customer[customer] > 1:
            loyal_customers_dict[customer] = quantity_per_customer[customer]
    return loyal_customers_dict

product_revenue = create_product_revenue_dict(sales_data)
customer_spending = create_customer_spending_dict(sales_data)
add_total_price(sales_data)
high_value_transactions = [transaction for transaction in sales_data if transaction["total_price"] > 500]
loyal_customers = create_loyalty_dict(sales_data)

print(product_revenue)
print(customer_spending)
print(loyal_customers)



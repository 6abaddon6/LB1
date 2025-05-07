def calculate_sales_statistics(sales_data):
    """
    Приймає список словників, що представляють продажі, та обчислює статистику доходів.

    Args:
        sales_data (list): Список словників, де кожен словник має ключі:
                           "продукт" (str), "кількість" (int), "ціна" (float).

    Returns:
        tuple: Кортеж, що містить:
            - dict: Словник, де ключі - назви продуктів, а значення - загальний дохід від їх продажу.
            - list: Список назв продуктів, що принесли дохід більший ніж 1000.
    """
    product_total_revenue = {}
    high_revenue_products = []

    for sale in sales_data:
        product = sale["продукт"]
        quantity = sale["кількість"]
        price = sale["ціна"]
        revenue = quantity * price

        product_total_revenue[product] = product_total_revenue.get(product, 0) + revenue

    for product, total_revenue in product_total_revenue.items():
        if total_revenue > 1000:
            high_revenue_products.append(product)

    return product_total_revenue, high_revenue_products

# Приклад використання:
sales = [
    {"продукт": "яблука", "кількість": 50, "ціна": 25.50},
    {"продукт": "банани", "кількість": 100, "ціна": 12.00},
    {"продукт": "яблука", "кількість": 30, "ціна": 25.50},
    {"продукт": "молоко", "кількість": 20, "ціна": 40.00},
    {"продукт": "хліб", "кількість": 150, "ціна": 8.75},
    {"продукт": "банани", "кількість": 80, "ціна": 12.00},
    {"продукт": "кава", "кількість": 10, "ціна": 120.00},
    {"продукт": "чай", "кількість": 25, "ціна": 55.00},
    {"продукт": "яблука", "кількість": 60, "ціна": 26.00},
]

total_revenue_by_product, high_revenue_product_list = calculate_sales_statistics(sales)

print("Загальний дохід для кожного продукту:")
for product, revenue in total_revenue_by_product.items():
    print(f"- {product}: {revenue:.2f} грн.")

print("\nПродукти, що принесли дохід більший ніж 1000 грн.:")
if high_revenue_product_list:
    print(high_revenue_product_list)
else:
    print("Немає продуктів з доходом більшим ніж 1000 грн.")
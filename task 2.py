class Inventory:
    def __init__(self, initial_inventory=None):
        if initial_inventory is None:
            self.inventory = {}
        else:
            self.inventory = initial_inventory.copy()

    def update_inventory(self, product_name, quantity_change):

        if product_name in self.inventory:
            self.inventory[product_name] += quantity_change
            if self.inventory[product_name] < 0:
                print(f"Увага: Кількість продукту '{product_name}' стала від'ємною ({self.inventory[product_name]}).")
            elif self.inventory[product_name] == 0:
                del self.inventory[product_name]  # Видаляємо продукт, якщо кількість стала нуль
        else:
            if quantity_change > 0:
                self.inventory[product_name] = quantity_change
            else:
                print(f"Помилка: Продукт '{product_name}' відсутній на складі, неможливо видалити.")

    def get_low_stock_products(self, threshold=5):

        low_stock = [product for product, quantity in self.inventory.items() if quantity < threshold]
        return low_stock

    def display_inventory(self):
        print("\nПоточний стан інвентарю:")
        if self.inventory:
            for product, quantity in self.inventory.items():
                print(f"- {product}: {quantity} од.")
        else:
            print("Інвентар порожній.")

# Приклад використання:
initial_stock = {"яблука": 10, "банани": 20, "молоко": 5, "хліб": 15}
warehouse = Inventory(initial_stock)

warehouse.display_inventory()

# Додавання продуктів
warehouse.update_inventory("яблука", 5)
warehouse.update_inventory("апельсини", 12)
warehouse.display_inventory()

# Видалення продуктів
warehouse.update_inventory("банани", -8)
warehouse.update_inventory("молоко", -7)
warehouse.display_inventory()

# Отримання списку продуктів з низьким запасом
low_stock_list = warehouse.get_low_stock_products()
print("\nПродукти з низьким запасом (менше 5):", low_stock_list)

# Спроба видалити відсутній продукт
warehouse.update_inventory("печиво", -3)

warehouse.display_inventory()

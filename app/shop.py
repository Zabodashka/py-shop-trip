import datetime
from typing import Dict


class Shop:
    def __init__(self, name: str, location: list, products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer_name: str, product_cart: Dict[str, int]) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.isoformat()}")
        print(f"Thank you, {customer_name}!")
        total_cost = 0.0
        for product, count in product_cart.items():
            price = self.products.get(product, 0) * count
            total_cost += price
            print(f"{count} {product}s for ${price:.2f}")
        print(f"Total cost is ${total_cost:.2f}")
        print("See you again!")

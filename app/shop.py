from typing import Dict
from datetime import datetime


class Shop:
    def __init__(
        self, name: str, location: list[int], products: Dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(
        self, customer_name: str, product_cart: Dict[str, int]
    ) -> None:
        now = datetime.now()
        total = sum(self.products[p] * q for p, q in product_cart.items())
        print()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            print(f"{quantity} {product}(s) for {price} dollars")
        print(f"Total cost is {total} dollars")
        print("See you again!")
        print()

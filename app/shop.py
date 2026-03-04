import datetime
from typing import Dict


class Shop:
    def __init__(self, name: str, location: list, products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self) -> None:
        now = datetime.datetime.now()
        print(f"Receipt from {self.name} at {now.isoformat()}")
        for product, price in self.products.items():
            print(f"{product}s: ${price:.2f}")

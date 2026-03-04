import datetime
from typing import Dict


class Shop:
    """Shop with name, location, and products."""

    def __init__(self, name: str, location: list[int],
                 products: Dict[str, float]) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, cart: Dict[str, int]) -> None:
        """Print receipt for the given cart."""
        print(f"Receipt for {datetime.datetime.now()}")
        total = 0.0
        for product, amount in cart.items():
            price = self.products[product] * amount
            total += price
            print(f"{amount} {product}s: ${price:.2f}")
        print(f"Total: ${total:.2f}")

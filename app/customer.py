from typing import Dict
from app.car import Car
from app.shop import Shop


class Customer:
    """Customer with a car, location, money, and shopping list."""

    def __init__(self, name: str, product_cart: Dict[str, int],
                 location: list[int], money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        """Calculate fuel cost for a trip to the shop and back."""
        dx = self.location[0] - shop.location[0]
        dy = self.location[1] - shop.location[1]
        distance = (dx**2 + dy**2)**0.5 * 2  # round trip
        return (distance / 100) * self.car.fuel_consumption * fuel_price

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        """Make a trip and buy products if enough money."""
        cost = self.trip_cost(shop, fuel_price)
        if self.money < cost:
            print(
                f"{self.name} doesn't have enough money to make a purchase "
                "in any shop"
            )
            return

        self.money -= cost
        for product, amount in self.product_cart.items():
            price = shop.products[product] * amount
            self.money -= price
            print(f"{amount} {product}s: ${price:.2f}")

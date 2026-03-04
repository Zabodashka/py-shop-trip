from typing import Dict
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self, name: str, money: float, location: list, product_cart: Dict[str, int],
        car: Car
    ) -> None:
        self.name = name
        self.money = money
        self.location = location
        self.product_cart = product_cart
        self.car = car

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = ((self.location[0] - shop.location[0]) ** 2 +
                    (self.location[1] - shop.location[1]) ** 2) ** 0.5
        return distance * self.car.fuel_consumption / 100 * fuel_price

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        cost = self.trip_cost(shop, fuel_price)
        if self.money >= cost:
            for product, count in self.product_cart.items():
                if product in shop.products:
                    price = shop.products[product] * count
                    print(f"{count} {product}s: ${price:.2f}")
                    self.money -= price
            self.money -= cost

from typing import Dict, List
from .car import Car
from .shop import Shop
import math


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: Dict[str, int],
        location: List[int],
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, other_location: List[int]) -> float:
        return math.hypot(
            self.location[0] - other_location[0],
            self.location[1] - other_location[1],
        )

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_needed = distance * self.car.fuel_consumption / 100
        cost_to_shop = fuel_needed * fuel_price
        product_cost = sum(
            shop.products[p] * q for p, q in self.product_cart.items()
        )
        return round(cost_to_shop * 2 + product_cost, 2)

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        distance = self.distance_to(shop.location)
        fuel_needed = distance * self.car.fuel_consumption / 100
        cost_to_shop = fuel_needed * fuel_price
        product_cost = sum(
            shop.products[p] * q for p, q in self.product_cart.items()
        )
        total_trip_cost = cost_to_shop * 2 + product_cost

        self.location = shop.location
        print(f"{self.name} rides to {shop.name}")

        shop.print_receipt(self.name, self.product_cart)

        self.money -= total_trip_cost
        self.money = round(self.money, 2)
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars")
        print()

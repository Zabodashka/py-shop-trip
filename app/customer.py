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
        round_trip_fuel = distance * 2 * self.car.fuel_consumption / 100 * fuel_price
        products_cost = sum(shop.products.get(p, 0) * c
                            for p, c in self.product_cart.items())
        return round_trip_fuel + products_cost

    def go_shopping(self, shop: Shop, fuel_price: float) -> None:
        total_cost = self.trip_cost(shop, fuel_price)
        if self.money < total_cost:
            print(
                f"{self.name} doesn't have enough money to make a purchase "
                "in any shop"
            )
            return

        distance = ((self.location[0] - shop.location[0]) ** 2 +
                    (self.location[1] - shop.location[1]) ** 2) ** 0.5
        fuel_cost = distance * 2 * self.car.fuel_consumption / 100 * fuel_price
        print(f"{self.name} rides to {shop.name}")
        shop.print_receipt(self.name, self.product_cart)
        self.money -= total_cost
        self.location = shop.location
        print(f"{self.name} rides home")
        print(f"{self.name} has {self.money:.2f} dollars left\n")

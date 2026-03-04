import json
import os
from typing import Any, Dict, List
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    config_path = os.path.join(os.path.dirname(__file__), "config.json")
    with open(config_path) as file:
        config: Dict[str, Any] = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    shops: List[Shop] = [Shop(**s) for s in config["shops"]]
    customers: List[Customer] = []

    for cust_data in config["customers"]:
        car_data = cust_data.pop("car")
        customer_car = Car(**car_data)
        customer = Customer(car=customer_car, **cust_data)
        customers.append(customer)

    for customer in customers:
        print(f"{customer.name} has {customer.money:.2f} dollars")
        trips = [(customer.trip_cost(shop, fuel_price), shop) for shop in shops]
        trips.sort(key=lambda t: t[0])
        for total_cost, shop in trips:
            if customer.money >= total_cost:
                customer.go_shopping(shop, fuel_price)
                break
        else:
            print(
                f"{customer.name} doesn't have enough money to make a purchase "
                "in any shop"
            )


if __name__ == "__main__":
    shop_trip()

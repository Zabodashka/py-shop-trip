class Car:
    """Car with brand and fuel consumption per 100 km."""

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

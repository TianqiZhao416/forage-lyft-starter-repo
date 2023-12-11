from abc import ABC

from car import Car

class CarriganTire():
    def __init__(tires) -> None:
        self.tires = tires
    def need_tire_service(self):
        for tire in self.tires:
            if tire > 0.9:
                return True
        return False
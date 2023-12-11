from abc import ABC

from car import Car

class OctoprimeTire():
    def __init__(self, tires) -> None:
        self.tires = tires
    def tires_need_service(self):
        sum = 0
        for tire in self.tires:
            sum += tire
        if sum>=3:
            return True
        return False
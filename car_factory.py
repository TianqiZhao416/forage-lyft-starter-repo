
from abc import ABC, abstractmethod

from car import Car

from battery.nubbin_battery import Nubbin_battery
from battery.spindler_battery import Spindler_battery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from tire.carrigan_tires import CarriganTire
from tire.octoprime_tires import OctoprimeTire


class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = Spindler_battery(last_service_date, current_date)
        return Car(engine, battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        engine = WilloughbyEngine( current_mileage,last_service_mileage)
        battery = Spindler_battery(last_service_date, current_date)
        return Car(engine, battery)

    def create_palindrome(current_date, last_service_date, warning_light):
        engine = SternmanEngine(warning_light)
        battery = Spindler_battery(last_service_date, current_date)
        return Car(engine, battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = Nubbin_battery(last_service_date, current_date)
        return Car(engine, battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tire):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = Nubbin_battery(last_service_date, current_date)
        return Car(engine, battery)
    

from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, engine, battery):
        # self.last_service_date = last_service_date
        self.engine = engine
        self.battery = battery

    # @abstractmethod
    def needs_service(self):
        return self.engine.needs_service() or self.battery.battery_should_be_serviced()

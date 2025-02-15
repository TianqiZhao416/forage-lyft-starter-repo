from abc import ABC

from car import Car

from datetime import datetime


class Nubbin_battery():
    def __init__(self, last_service_date, current_date):
        # super().__init__(last_service_date)
        self.last_service_date = last_service_date
        self.current_date = current_date

    def battery_should_be_serviced(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date< datetime.today().date():
            return True
        else:
            return False
from datetime import date
from battery_interface import BatteryInterface

class SpindlerBattery(BatteryInterface):

    YEAR_SERVICING_THRESHOLD = 2
    DAYS_IN_A_YEAR = 365

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        # Based on model implementation
        next_service_date = self.last_service_date.replace(
            year = self.last_service_date.year + self.YEAR_SERVICING_THRESHOLD
        )
        return self.current_date >= next_service_date

from datetime import date
from battery_interface import BatteryInterface

class NubbinBattery(BatteryInterface):

    YEAR_SERVICING_THRESHOLD = 4
    DAYS_IN_A_YEAR = 365

    def __init__(self, last_service_date: date, current_date: date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        days_since_service = (self.current_date - self.last_service_date).days
        years_since_service = days_since_service // self.DAYS_IN_A_YEAR  # Does not account for leap years
        return years_since_service >= self.YEAR_SERVICING_THRESHOLD

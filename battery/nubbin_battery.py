from battery_interface import BatteryInterface

class NubbinBattery(BatteryInterface):

    YEAR_SERVICING_THRESHOLD = 4

    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= self.YEAR_SERVICING_THRESHOLD

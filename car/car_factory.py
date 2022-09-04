from datetime import date
from car import Car
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from calliope import Calliope
from glissade import Glissade
from palindrome import Palindrome
from rorschach import Rorschach
from thovex import Thovex

class CarFactory():
    def create_calliope(self, current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int) -> Car:
        return Calliope(CapuletEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date))

    def create_glissade(self, current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int) -> Car:
        return Glissade(WilloughbyEngine(last_service_mileage, current_mileage),
            SpindlerBattery(last_service_date, current_date))

    def create_palindrome(self, current_date: date, last_service_date: date,
        warning_light_on: bool) -> Car:
        return Palindrome(SternmanEngine(warning_light_on),
            SpindlerBattery(last_service_date, current_date))

    def create_rorschach(self, current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int) -> Car:
        return Rorschach(WilloughbyEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date))

    def create_thovex(self, current_date: date, last_service_date: date,
        current_mileage: int, last_service_mileage: int) -> Car:
        return Thovex(CapuletEngine(last_service_mileage, current_mileage),
            NubbinBattery(last_service_date, current_date))

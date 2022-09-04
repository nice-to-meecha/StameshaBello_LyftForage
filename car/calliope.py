from car import Car
from battery.battery_interface import BatteryInterface
from engine.engine_interface import EngineInterface

class Calliope(Car):
    def __init__(self, engine: EngineInterface, battery: BatteryInterface):
        super().__init__(engine, battery)

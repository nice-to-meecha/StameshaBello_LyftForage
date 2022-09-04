from serviceable import Serviceable
from battery.battery_interface import BatteryInterface
from engine.engine_interface import EngineInterface

class Car(Serviceable):

    def __init__(self, engine: EngineInterface, battery: BatteryInterface):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

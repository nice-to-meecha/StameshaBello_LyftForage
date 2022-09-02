from engine_interface import EngineInterface

class SternmanEngine(EngineInterface):
    
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
        
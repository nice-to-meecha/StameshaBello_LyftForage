import abc

class BatteryInterface(abc.ABC):

    @abc.abstractmethod
    def needs_service() -> bool:
        pass
    
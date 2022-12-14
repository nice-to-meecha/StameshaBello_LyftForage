import abc

class EngineInterface(abc.ABC):

    @abc.abstractmethod
    def needs_service() -> bool:
        pass

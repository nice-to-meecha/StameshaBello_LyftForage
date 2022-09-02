import abc

class EngineInterface(abc.ABC):

    @abc.abstractmethod
    def needs_servicing() -> bool:
        pass
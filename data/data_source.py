from abc import ABC, abstractmethod

from logic.models.grammer import Grammer

class DataSource(ABC):
    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def readGrammer(self) -> Grammer:
        pass

    @abstractmethod
    def write(self, data):
        pass
from abc import abstractmethod, ABC
from PIL.Image import Image

class Text2Image(ABC):
    @property
    @abstractmethod
    def image(self) -> Image:
        ...

    @property
    @abstractmethod
    def text(self) -> str:
        ...

    @abstractmethod
    def resault(self) -> Image:
        ...

    @abstractmethod
    def genrate(self) -> None:
        ...
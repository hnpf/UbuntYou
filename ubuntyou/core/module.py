import abc
from rich.console import Console
console = Console()

class Module(abc.ABC):
    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Friendly name of the module."""
        pass

    @property
    @abc.abstractmethod
    def description(self) -> str:
        """Short description of what it does."""
        pass

    @abc.abstractmethod
    def apply(self) -> bool:
        """Apply the actual logic. returns True if successful."""
        pass

    @abc.abstractmethod
    def revert(self) -> bool:
        """Revert the changes. returns True if successful."""
        pass

    @abc.abstractmethod
    def is_applied(self) -> bool:
        """checks if the logic is already active."""
        pass

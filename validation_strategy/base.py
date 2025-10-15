from __future__ import annotations
from abc import ABC, abstractmethod

class Context():
    """
    The context defines the interface of interest to clients
    """

    def __init__(self, strategy: Strategy, input_data: str) -> None:
        """
        Typically, a Context accepts a strategy through a constructor as well
        provides a setter for its runtime changes.
        """

        self._strategy = strategy
        self.input_data = input_data

    @property
    def strategy(self) -> Strategy:
        """
        The context stores a reference to one of the Strategy objects. The context does not know
        a specific class of strategies. It should work with all strategies
        through the Strategy interface.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        The Normal Context allows you to change the Strategy object at runtime.
        """

        self._strategy = strategy

    def do_logic(self) -> None:
        """
        Instead of implementing multiple versions yourself
        algorithm, the Context delegates some work of the Strategy object.
        """

        result = self._strategy.do_algorithm(validate_field=self.input_data)
        return result


class Strategy(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    some algorithm.

    The context uses this interface to call the algorithm defined
    Specific strategies.
    """

    @abstractmethod
    def do_algorithm(self, validate_field: str):
        pass
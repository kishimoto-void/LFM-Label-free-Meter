# Base Observer

from abc import ABC, abstractmethod
from typing import Any

class BaseObserver(ABC):
    """全Observerの基底クラス"""
    @abstractmethod
    def measure(self, state: Any) -> float:
        """状態に対する計測値を返す"""
        pass
    
    @property
    def name(self) -> str:
        return self.__class__.__name__.lower().replace("observer", "")

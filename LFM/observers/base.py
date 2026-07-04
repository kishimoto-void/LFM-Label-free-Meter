# Base Observer / Utilities

import numpy as np
from abc import ABC, abstractmethod
from typing import Any, Dict

def clean_array(arr: np.ndarray) -> np.ndarray:
    """NaN/infを除去する共通ユーティリティ"""
    return arr[np.isfinite(arr)]

class BaseObserver(ABC):
    """全Observerの基底クラス"""
    @abstractmethod
    def measure(self, storage: Any, tick: int, **kwargs) -> Dict:
        """storageとtickを受け取り計測"""
        pass
    
    @property
    def name(self) -> str:
        return self.__class__.__name__.lower().replace("observer", "")

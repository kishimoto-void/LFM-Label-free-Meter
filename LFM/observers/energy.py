# Energy Observer

from .base import BaseObserver
from typing import Any

class EnergyObserver(BaseObserver):
    """エネルギー / tension field 強度計測"""
    def measure(self, state: Any) -> float:
        # TODO: VGE/CUBE互換
        return 0.0

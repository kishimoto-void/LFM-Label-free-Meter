# Position Observer (将来拡張用)

from .base import BaseObserver
from typing import Any

class PositionObserver(BaseObserver):
    """状態位置・embedding空間内位置計測"""
    def measure(self, state: Any) -> float:
        return 0.0

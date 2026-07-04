# Observer登録管理
from typing import Dict, Callable, Any
from .observers.velocity import velocity_statistics
from .observers.topology import topology_statistics
from .observers.energy import energy_statistics
# 他のObserverも随時追加

class ObserverRegistry:
    def __init__(self):
        self.default_observers: Dict[str, Callable] = {
            "velocity_stats": velocity_statistics,
            "topology_stats": topology_statistics,
            "energy_stats": energy_statistics,
            # "lifetime_stats": lifetime_statistics,
            # 必要に応じて追加
        }
    
    def get_default(self) -> Dict[str, Callable]:
        """デフォルトObserver群"""
        return self.default_observers.copy()

    def register_custom(self, name: str, observer: Callable):
        self.default_observers[name] = observer

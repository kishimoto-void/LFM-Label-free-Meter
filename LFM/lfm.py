from typing import Dict, Any, List
from .registry import ObserverRegistry

class LFM:
    """
    Label-Free Meter (LFM)
    
    Principles
    ----------
    1. No interpretation, no semantic labels
    2. Observation facts only
    3. Storage-only dependency
    4. Reproducible & consistent output format
    """

    def __init__(self, version: str = "0.1.0"):
        self.version = version
        self.registry = ObserverRegistry()
        self.observers: Dict[str, Any] = {}

    def register(self, name: str, observer_callable):
        """Observerを登録"""
        self.observers[name] = observer_callable

    def measure(self, observer_name: str, storage, tick: int, **kwargs) -> Dict:
        """単一観測"""
        if observer_name not in self.observers:
            raise KeyError(f"Observer '{observer_name}' not registered.")
        
        data = self.observers[observer_name](storage, tick, **kwargs)
        
        return {
            "meta": {
                "tick": tick,
                "observer": observer_name,
                "version": self.version,
                "seed": getattr(storage, "seed", None)
            },
            "data": data
        }

    def measure_all(self, storage, tick: int) -> List[Dict]:
        """登録済み全Observerを実行"""
        results = []
        for name in self.observers:
            try:
                results.append(self.measure(name, storage, tick))
            except Exception as e:
                # 1つのObserver失敗でも全体を止めない（堅牢性）
                print(f"Warning: Observer '{name}' failed at tick {tick}: {e}")
        return results

# LFM本体クラス

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional

@dataclass
class LFMConfig:
    """LFM設定"""
    metrics: List[str] = field(default_factory=lambda: ["velocity", "topology", "energy", "lifetime"])
    window_size: int = 1000
    decay_factor: float = 0.95

class LabelFreeMeter:
    """Label-Free Meter 本体
    ラベルなしで状態の質・安定性・ダイナミクスを計測"""
    def __init__(self, config: Optional[LFMConfig] = None):
        self.config = config or LFMConfig()
        self.observers = {}
        self.history = []
        
    def register_observer(self, name: str, observer):
        self.observers[name] = observer
    
    def measure(self, state: Any) -> Dict[str, float]:
        """状態に対して全observerで計測"""
        results = {}
        for name, obs in self.observers.items():
            if name in self.config.metrics:
                results[name] = obs.measure(state)
        self.history.append(results)
        return results

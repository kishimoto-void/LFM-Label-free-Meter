# Velocity Observer
import numpy as np
from scipy import stats
from .base import clean_array
from typing import Dict, Any

def velocity_statistics(storage: Any, tick: int, **kwargs) -> Dict:
    """Velocity関連統計量"""
    v_alive = clean_array(storage.arrays["v"][storage.arrays["alive"]])
    
    if len(v_alive) == 0:
        return {"n_alive": 0}
    
    return {
        "n_alive": int(len(v_alive)),
        "mean": float(np.mean(v_alive)),
        "std": float(np.std(v_alive, ddof=1)),
        "min": float(np.min(v_alive)),
        "max": float(np.max(v_alive)),
        "q25": float(np.percentile(v_alive, 25)),
        "q50": float(np.percentile(v_alive, 50)),
        "q75": float(np.percentile(v_alive, 75)),
        "skewness": float(stats.skew(v_alive)),
        "kurtosis": float(stats.kurtosis(v_alive))
    }

# LFM登録用ラッパー（callable）
def velocity_observer(storage: Any, tick: int, **kwargs) -> Dict:
    return velocity_statistics(storage, tick, **kwargs)

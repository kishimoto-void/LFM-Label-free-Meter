# Observer登録管理

from typing import Dict
from .observers.base import BaseObserver

class ObserverRegistry:
    """Observerの登録・管理"""
    def __init__(self):
        self.observers: Dict[str, BaseObserver] = {}
    
    def register(self, name: str, observer: BaseObserver):
        self.observers[name] = observer
    
    def get(self, name: str):
        return self.observers.get(name)
    
    def list_all(self):
        return list(self.observers.keys())

# Base Exporter

from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseExporter(ABC):
    @abstractmethod
    def export(self, data: Dict[str, Any], **kwargs):
        pass

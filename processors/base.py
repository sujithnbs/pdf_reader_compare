from abc import ABC, abstractmethod
from pathlib import Path
class BaseProcessor(ABC):
    name = 'base'

    def __init__(self, output_dir:Path):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    @abstractmethod
    def process(self, pdf_path:Path):
        """
        Convert pdf_path => plain text file path
        Return path to produced text file.
        """
        pass

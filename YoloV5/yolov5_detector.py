from dataclasses import dataclass
from typing import Union, Tuple
import pandas as pd
import torch
import numpy as np


@dataclass
class Yolov5Detector:
    model_path: str
    confidence_threshold: float = 0.2

    def __post_init__(self) -> None:
        self.model = torch.hub.load("ultralytics/yolov5", "custom", fr"{self.model_path}", force_reload=True)
        self.model.conf = self.confidence_threshold

    def detect(self, image: Union[str, np.array]) -> Tuple[np.array, pd.DataFrame]:
        results = self.model([image])

        return np.squeeze(results.render()), results.pandas().xyxy[0]

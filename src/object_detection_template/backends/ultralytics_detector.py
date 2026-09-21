"""Ultralytics implementation of the Detector protocol."""

from __future__ import annotations

from pathlib import Path

from object_detection_template.domain import BoundingBox, Detection


class UltralyticsDetector:
    """Adapt Ultralytics prediction results to the template domain."""

    def __init__(self, model: str | Path) -> None:
        try:
            from ultralytics import YOLO
        except ImportError as exc:
            raise RuntimeError(
                "Install the optional backend with: uv sync --extra ultralytics"
            ) from exc
        self._model = YOLO(str(model))

    def detect(self, source: Path) -> tuple[Detection, ...]:
        results = self._model.predict(source=str(source), verbose=False)
        detections: list[Detection] = []
        for result in results:
            if result.boxes is None:
                continue
            names = result.names
            for coordinates, confidence, class_id in zip(
                result.boxes.xyxy.tolist(),
                result.boxes.conf.tolist(),
                result.boxes.cls.tolist(),
                strict=True,
            ):
                x_min, y_min, x_max, y_max = coordinates
                detections.append(
                    Detection(
                        label=str(names[int(class_id)]),
                        confidence=float(confidence),
                        box=BoundingBox(
                            x_min=float(x_min),
                            y_min=float(y_min),
                            x_max=float(x_max),
                            y_max=float(y_max),
                        ),
                    )
                )
        return tuple(detections)

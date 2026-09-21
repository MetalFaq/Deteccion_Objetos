"""Framework-neutral inspection orchestration."""

from __future__ import annotations

from collections.abc import Mapping
from pathlib import Path

from object_detection_template.domain import InspectionResult, TextObservation
from object_detection_template.ports import Detector, TextRecognizer


class InspectionPipeline:
    """Run detection and optional per-class text recognition."""

    def __init__(
        self,
        detector: Detector,
        *,
        confidence_threshold: float = 0.5,
        text_readers: Mapping[str, TextRecognizer] | None = None,
    ) -> None:
        if not 0.0 <= confidence_threshold <= 1.0:
            raise ValueError("confidence_threshold must be between 0 and 1")
        self._detector = detector
        self._confidence_threshold = confidence_threshold
        self._text_readers = dict(text_readers or {})

    def run(self, source: str | Path) -> InspectionResult:
        source_path = Path(source)
        detections = tuple(
            sorted(
                (
                    detection
                    for detection in self._detector.detect(source_path)
                    if detection.confidence >= self._confidence_threshold
                ),
                key=lambda detection: detection.confidence,
                reverse=True,
            )
        )

        observations: list[TextObservation] = []
        for detection in detections:
            reader = self._text_readers.get(detection.label)
            if reader is None:
                continue
            text = reader.read(source_path, detection)
            if text and text.strip():
                observations.append(TextObservation(detection=detection, text=text.strip()))

        return InspectionResult(
            source=source_path,
            detections=detections,
            text_observations=tuple(observations),
        )

"""Stable domain objects shared by detectors, OCR readers, and applications."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True, slots=True)
class BoundingBox:
    """Axis-aligned bounding box in source-image pixel coordinates."""

    x_min: float
    y_min: float
    x_max: float
    y_max: float

    def __post_init__(self) -> None:
        if self.x_min < 0 or self.y_min < 0:
            raise ValueError("Bounding-box coordinates must be non-negative")
        if self.x_max <= self.x_min or self.y_max <= self.y_min:
            raise ValueError("Bounding box must have positive width and height")

    @property
    def width(self) -> float:
        return self.x_max - self.x_min

    @property
    def height(self) -> float:
        return self.y_max - self.y_min


@dataclass(frozen=True, slots=True)
class Detection:
    """A normalized detection returned by any supported backend."""

    label: str
    confidence: float
    box: BoundingBox

    def __post_init__(self) -> None:
        if not self.label.strip():
            raise ValueError("Detection label cannot be empty")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Detection confidence must be between 0 and 1")


@dataclass(frozen=True, slots=True)
class TextObservation:
    """Text recognized inside one detected region."""

    detection: Detection
    text: str


@dataclass(frozen=True, slots=True)
class InspectionResult:
    """Backend-independent result for one source image."""

    source: Path
    detections: tuple[Detection, ...] = field(default_factory=tuple)
    text_observations: tuple[TextObservation, ...] = field(default_factory=tuple)

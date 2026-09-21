"""Protocols implemented by concrete computer-vision backends."""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import Protocol

from object_detection_template.domain import Detection


class Detector(Protocol):
    """Detect objects in one image without exposing framework-specific results."""

    def detect(self, source: Path) -> Sequence[Detection]:
        """Return zero or more detections for ``source``."""


class TextRecognizer(Protocol):
    """Read text from one previously detected region."""

    def read(self, source: Path, detection: Detection) -> str | None:
        """Return normalized text or ``None`` when no text is accepted."""

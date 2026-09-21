"""Pillow and Tesseract implementation of the TextRecognizer protocol."""

from __future__ import annotations

from pathlib import Path

from object_detection_template.domain import Detection


class TesseractReader:
    """Crop one detection and delegate OCR to the system Tesseract binary."""

    def __init__(self, *, language: str | None = None, config: str = "--oem 3 --psm 6") -> None:
        self._language = language
        self._config = config

    def read(self, source: Path, detection: Detection) -> str | None:
        try:
            import pytesseract
            from PIL import Image
        except ImportError as exc:
            raise RuntimeError("Install OCR support with: uv sync --extra ocr") from exc

        box = detection.box
        with Image.open(source) as image:
            crop = image.crop(
                (
                    int(box.x_min),
                    int(box.y_min),
                    int(box.x_max),
                    int(box.y_max),
                )
            )
            text = pytesseract.image_to_string(
                crop,
                lang=self._language,
                config=self._config,
            )
        normalized = " ".join(text.split())
        return normalized or None

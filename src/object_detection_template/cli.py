"""Command-line interface for the optional Ultralytics adapter."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Object-detection project template")
    subparsers = parser.add_subparsers(dest="command", required=True)

    inspect_parser = subparsers.add_parser("inspect", help="Inspect one image")
    inspect_parser.add_argument("--model", required=True, help="Model name or local path")
    inspect_parser.add_argument("--source", type=Path, required=True, help="Input image")
    inspect_parser.add_argument("--threshold", type=float, default=0.5)
    inspect_parser.add_argument(
        "--ocr-label",
        action="append",
        default=[],
        help="Detection label to pass to Tesseract; may be repeated",
    )
    return parser


def _inspect(args: argparse.Namespace) -> int:
    from object_detection_template.backends.tesseract_reader import TesseractReader
    from object_detection_template.backends.ultralytics_detector import UltralyticsDetector
    from object_detection_template.pipeline import InspectionPipeline

    readers = {label: TesseractReader() for label in args.ocr_label}
    pipeline = InspectionPipeline(
        UltralyticsDetector(args.model),
        confidence_threshold=args.threshold,
        text_readers=readers,
    )
    result = pipeline.run(args.source)
    print(json.dumps(asdict(result), indent=2, default=str, ensure_ascii=False))
    return 0


def main() -> int:
    args = _build_parser().parse_args()
    if args.command == "inspect":
        return _inspect(args)
    raise AssertionError(f"Unhandled command: {args.command}")


if __name__ == "__main__":
    raise SystemExit(main())

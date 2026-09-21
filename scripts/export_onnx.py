"""Export an Ultralytics checkpoint to a selected deployment format."""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", required=True, help="Local trusted checkpoint")
    parser.add_argument("--output-format", default="onnx")
    args = parser.parse_args()

    try:
        from ultralytics import YOLO
    except ImportError as exc:
        raise SystemExit("Install the backend with: uv sync --extra ultralytics") from exc

    model = YOLO(args.model)
    model.export(format=args.output_format)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

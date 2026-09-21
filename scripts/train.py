"""Minimal Ultralytics training entry point; replace defaults for each project."""

from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Dataset YAML")
    parser.add_argument("--model", default="yolo26n.pt")
    parser.add_argument("--epochs", type=int, default=50)
    parser.add_argument("--image-size", type=int, default=640)
    args = parser.parse_args()

    try:
        from ultralytics import YOLO
    except ImportError as exc:
        raise SystemExit("Install the backend with: uv sync --extra ultralytics") from exc

    model = YOLO(args.model)
    model.train(data=args.data, epochs=args.epochs, imgsz=args.image_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

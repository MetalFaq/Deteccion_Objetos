"""Reusable contracts and orchestration for object detection projects."""

from object_detection_template.domain import BoundingBox, Detection, InspectionResult
from object_detection_template.pipeline import InspectionPipeline

__all__ = ["BoundingBox", "Detection", "InspectionPipeline", "InspectionResult"]

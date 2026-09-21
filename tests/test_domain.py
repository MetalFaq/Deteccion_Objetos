import pytest

from object_detection_template.domain import BoundingBox, Detection


def test_bounding_box_rejects_inverted_coordinates() -> None:
    with pytest.raises(ValueError, match="positive width"):
        BoundingBox(x_min=10, y_min=2, x_max=5, y_max=8)


def test_detection_rejects_invalid_confidence() -> None:
    box = BoundingBox(x_min=0, y_min=0, x_max=10, y_max=10)
    with pytest.raises(ValueError, match="between 0 and 1"):
        Detection(label="object", confidence=1.5, box=box)

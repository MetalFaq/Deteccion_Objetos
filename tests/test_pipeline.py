from pathlib import Path

from object_detection_template.domain import BoundingBox, Detection
from object_detection_template.pipeline import InspectionPipeline


class FakeDetector:
    def detect(self, source: Path) -> tuple[Detection, ...]:
        assert source == Path("sample.jpg")
        return (
            Detection("label", 0.91, BoundingBox(0, 0, 20, 10)),
            Detection("noise", 0.20, BoundingBox(5, 5, 8, 8)),
        )


class FakeReader:
    def read(self, source: Path, detection: Detection) -> str:
        assert source == Path("sample.jpg")
        assert detection.label == "label"
        return "  example text  "


def test_pipeline_filters_and_normalizes_results() -> None:
    pipeline = InspectionPipeline(
        FakeDetector(),
        confidence_threshold=0.5,
        text_readers={"label": FakeReader()},
    )

    result = pipeline.run("sample.jpg")

    assert [detection.label for detection in result.detections] == ["label"]
    assert [observation.text for observation in result.text_observations] == ["example text"]

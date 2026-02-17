import pytest
from pydantic import ValidationError
from models.student_model import StudentProfile, Confidence

def make_valid_profile():
    return {
        "student_id": "s1",
        "grade": 5,
        "subjects": {
            "math": {
                "algebra": {"mastery": 0.8, "confidence": "high"}
            },
            "science": {
                "physics": {"mastery": 0.5, "confidence": "medium"}
            }
        }
    }

class TestStudentModel:
    def test_valid_profile(self):
        data = make_valid_profile()
        profile = StudentProfile(**data)
        assert profile.student_id == "s1"
        assert profile.grade == 5
        assert "math" in profile.subjects
        assert profile.subjects["math"]["algebra"].mastery == pytest.approx(0.8)
        assert profile.subjects["math"]["algebra"].confidence == Confidence.high

    def test_mastery_out_of_range(self):
        data = make_valid_profile()
        data["subjects"]["math"]["algebra"]["mastery"] = 1.5
        with pytest.raises(ValidationError):
            StudentProfile(**data)

    def test_grade_too_small(self):
        data = make_valid_profile()
        data["grade"] = 0
        with pytest.raises(ValidationError):
            StudentProfile(**data)

    def test_invalid_confidence(self):
        data = make_valid_profile()
        data["subjects"]["math"]["algebra"]["confidence"] = "unknown"
        with pytest.raises(ValidationError):
            StudentProfile(**data)
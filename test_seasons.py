from seasons import convert
import pytest

def test_cs50_convert():
    assert convert("2024-09-08") =="Zero minutes"
    assert convert("2001-01-01") == "Twelve million, four hundred fifty-seven thousand, four hundred forty minutes"
    with pytest.raises(SystemExit):
        assert convert("2024-13-05")

def test_cs50_convert_invalid_date():
    with pytest.raises(SystemExit):
        convert("2024-02-30")
    with pytest.raises(SystemExit):
        convert("2024-13-01")


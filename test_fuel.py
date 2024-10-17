from fuel import convert
from fuel import gauge
import pytest



def test_fuel_convert():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("1/dog")
    with pytest.raises(ValueError):
        convert("cat/1")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    assert convert("3/4") == 75
    assert convert("3/8") == 38



def test_fuel_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(54) == "54%"
    assert gauge(33) == "33%"

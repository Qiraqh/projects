from numb3rs import validate


def test_numbers_invalid():
    assert validate('258.1.1.1') == False
    assert validate("127.0.1.") == False
    assert validate("1.258.1.1") == False
    assert validate("512.512.512.512") == False


def test_number_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_string():
    assert validate("cat") == False
    assert validate("abc") == False
    assert validate("abc.1.1.1") == False


from plates import is_valid


def test_is_valid_cs50():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False
    assert is_valid("PI3.14") == False
    assert is_valid("H") == False
    assert is_valid("OUTATIME") == False


def test_is_valid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("CS50500") == False



def test_is_valid_characters():
    assert is_valid("AB33 45") == False
    assert is_valid("CS50!") == False
    assert is_valid("HF.76") == False



def test_is_valid_valid():
    assert is_valid("HH40") == True
    assert is_valid("NFG40") == True
    assert is_valid("KGGG7") == True

def test_is_valid_numbers():
    assert is_valid("50CS") == False
    assert is_valid("05CS") == False
    assert is_valid("555CS") == False

def test_is_valid_first_2_letter():
    assert is_valid("C50") == False

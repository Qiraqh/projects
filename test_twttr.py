from twttr import shorten



def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("DAD") == "DD"

def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("dad") == "dd"

def test_cs50():
    assert shorten("Twitter") == "Twttr"
    assert shorten("What's your name?") == "Wht's yr nm?"
    assert shorten("CS50") == "CS50"

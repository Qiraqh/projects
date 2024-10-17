from bank import value



def test_cs50():
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0
    assert value("How you doing?") == 20
    assert value("Whats happening?") == 100

def test_cs50_lowercase():
    assert value("hello") == 0
    assert value("hello, Newman") == 0
    assert value("how you doing?") == 20
    assert value("whats happening?") == 100


def test_number():
    assert value("hello") == 0
    assert value("h3llo") == 20
    assert value("Whats happening 12?") == 100

from um import count


def test_count_cs50():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_count_valid():
    assert count("um um um") == 3
    assert count("Um um um") == 3
    assert count("um? um? um?") == 3
    assert count("Um? um? Um?") == 3

def test_count_invalid():
    assert count("umbrella") == 0
    assert count("aluminum") == 0
    assert count("summary") == 0
    assert count("Umbridge") == 0

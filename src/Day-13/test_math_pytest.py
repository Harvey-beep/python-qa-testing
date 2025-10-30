from utils import add

def test_add_positive_numbers():
    assert add(5, 5) == 10

def test_add_negative_numbers():
    assert add(-5, -9) == -14

def test_add_mixed_numbers():
    assert add(10, -5) == 5
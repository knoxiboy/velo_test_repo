from main import add, sub, mul

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(3, 1) == 2

def test_mul():
    assert mul(2, 3) == 6

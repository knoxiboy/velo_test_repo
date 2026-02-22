from main import add, sub, mul

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(3, 1) == 2

def test_mul():
    assert mul(2, 3) == 6


# Logical test cases: mathematical properties of add
def test_add_commutativity():
    """Adding a and b should equal adding b and a."""
    assert add(2, 5) == add(5, 2)
    assert add(-3, 7) == add(7, -3)


def test_add_identity():
    """Adding zero should not change the value."""
    assert add(10, 0) == 10
    assert add(0, -4) == -4


def test_add_inverse():
    """A number plus its additive inverse should equal zero."""
    assert add(5, -5) == 0
    assert add(-100, 100) == 0
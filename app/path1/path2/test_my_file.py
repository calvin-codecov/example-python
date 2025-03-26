from my_file import OtherCalculator


def test_add():
    assert OtherCalculator.add(1, 2) == 3.0
    assert OtherCalculator.add(1.0, 2.0) == 3.0
    assert OtherCalculator.add(0, 2.0) == 2.0
    assert OtherCalculator.add(2.0, 0) == 2.0
    assert OtherCalculator.add(-4, 2.0) == -2.0

def test_subtract():
    assert OtherCalculator.subtract(1, 2) == -1.0
    assert OtherCalculator.subtract(2, 1) == 1.0
    assert OtherCalculator.subtract(1.0, 2.0) == -1.0
    assert OtherCalculator.subtract(0, 2.0) == -2.0
    assert OtherCalculator.subtract(2.0, 0.0) == 2.0
    assert OtherCalculator.subtract(-4, 2.0) == -6.0

def test_multiply():
    assert OtherCalculator.multiply(1, 2) == 2.0
    assert OtherCalculator.multiply(1.0, 2.0) == 2.0
    assert OtherCalculator.multiply(0, 2.0) == 0.0
    assert OtherCalculator.multiply(2.0, 0.0) == 0.0
    assert OtherCalculator.multiply(-4, 2.0) == -8.0

def test_divide():
    # assert OtherCalculator.divide(1, 2) == 0.5
    assert OtherCalculator.divide(1.0, 2.0) == 0.5
    assert OtherCalculator.divide(0, 2.0) == 0
    assert OtherCalculator.divide(-4, 2.0) == -2.0
    # assert OtherCalculator.divide(2.0, 0.0) == 'Cannot divide by 0'

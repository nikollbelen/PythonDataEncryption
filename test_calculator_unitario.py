from calculator import Calculator

calculator = Calculator()

def test_add():
    result = calculator.add(5,3)
    assert result == 8

def test_sustract():
    result = calculator.sustract(8,2)
    assert result == 6

def test_multiply():
    result = calculator.multiply(4,3)
    assert result == 12
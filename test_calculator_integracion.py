from calculator import Calculator

def test_integracion():

    calculator = Calculator()

    # Operacion suma
    result = calculator.add(3,4)
    assert result == 7

    # Operacion resta
    result = calculator.sustract(6,3)
    assert result == 3

    # Operacion multiplicacion
    result = calculator.multiply(3,4)
    assert result == 12 
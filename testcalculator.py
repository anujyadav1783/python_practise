from calculator import calculatora

def test_calculator_two():
    assert calculatora(2)==4

def test_calculator_three():
    assert calculatora(3)==7

def test_calculator_negative_two():
    assert calculatora(-2)==4

def test_calculator_negative_three():
    assert calculatora(-3)==9



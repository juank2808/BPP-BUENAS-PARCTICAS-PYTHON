from ops import suma,resta,multiplicacion,division,cap_case

def test_suma():
    assert suma(20,10) == 30
def test_resta():
    assert resta(10,20) < 0
def test_multiplicacion():
    assert multiplicacion(10,20) == 200
def test_division():
    assert division(20,2) == 10    

def test_capital_case():
    assert cap_case('JUANK') == "Juank"

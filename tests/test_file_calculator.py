from calculator_pkg_jkc.file_calculator import FileCalculator
# alternate from ..file_calculator

def test_file_calculator():
    assert FileCalculator().sum_file() == 6

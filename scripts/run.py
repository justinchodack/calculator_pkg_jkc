from pathlib import Path

from calculator_pkg_jkc import Calculator
from calculator_pkg_jkc.file_calculator import FileCalculator

print(Calculator().add(1, 2))
FileCalculator().sum_file(Path("~/Desktop/nums.csv").expanduser())


# /*
#
# ### ⬜ WHITE-BOX TESTING (Flow & Branch Coverage)
#
# | # | Flow (Conditions)                         | Condition                                | Input         | Expected Output            |
# |---|-------------------------------------------|-------------------------------------------|---------------|----------------------------|
# | 1 | IF-1 (T)                                   | args is None                              | None          | MissingArgumentException   |
# | 2 | IF-1 (T)                                   | len(args) == 0                            | []            | MissingArgumentException   |
# | 3 | IF-1 (F), IF-2 (T)                         | len(args) > 1                             | ["2", "3"]  | Only1ArgumentException     |
# | 4 | IF-1 (F), IF-2 (F), TRY/EXCEPT (except)    | float(args[0]) raises ValueError          | ["abc"]      | NoPositiveNumberException  |
# | 5 | IF-1 (F), IF-2 (F), IF-3 (T)               | num <= 0                                  | ["0"]         | NoPositiveNumberException  |
# | 6 | IF-1 (F), IF-2 (F), FOR with divisor match | num % i == 0 for some i in range(2, num)  | ["4"]         | False                      |
# | 7 | IF-1 (F), IF-2 (F), FOR no divisor         | loop completes without divisible value    | ["5"]         | True                       |
#
# ### ⬛ BLACK-BOX TESTING (EP & Boundary Value Analysis)
#
# | # | Condition / Technique                              | Input                | Expected Output |
# |---|----------------------------------------------------|----------------------|-----------------|
# | 1 | BVA: Límite matemático (n = 1, no primo)          | ["1"]               | False           |
# | 2 | BVA: Primer número primo válido                    | ["2"]               | True            |
# | 3 | EP: Decimal positivo no entero (se trunca a int)  | ["2.9"]             | True            |
# | 4 | EP: Notación científica positiva                   | ["2e1"]             | False           |
# | 5 | EP: Valor extremadamente grande no primo           | ["1000000"]         | False           |
#
# */

import os
import sys

import pytest


CURRENT_DIR = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
SRC_DIR = os.path.join(PROJECT_ROOT, "src")

if SRC_DIR not in sys.path:
	sys.path.insert(0, SRC_DIR)

import Exception as exception_module

# Alias to satisfy isPrime.py dependency: "from Exceptions import ..."
sys.modules["Exceptions"] = exception_module

from Exception import (
	MissingArgumentException,
	NoPositiveNumberException,
	Only1ArgumentException,
)
from isPrime import is_prime


class TestIsPrime:
	@pytest.mark.parametrize(
		"args, expected",
		[
			(["4"], False),
			(["5"], True),
			(["1"], False),
			(["2"], True),
			(["2.9"], True),
			(["2e1"], False),
			(["1000000"], False),
		],
	)
	def test_returns_expected_boolean_for_valid_inputs(self, args, expected):
		# Arrange
		input_args = args

		# Act
		result = is_prime(input_args)

		# Assert
		assert result is expected

	@pytest.mark.parametrize(
		"args, expected_exception",
		[
			(None, MissingArgumentException),
			([], MissingArgumentException),
			(["2", "3"], Only1ArgumentException),
			(["abc"], NoPositiveNumberException),
			(["0"], NoPositiveNumberException),
		],
	)
	def test_raises_expected_exception_for_invalid_inputs(self, args, expected_exception):
		# Arrange
		input_args = args

		# Act & Assert
		with pytest.raises(expected_exception):
			is_prime(input_args)

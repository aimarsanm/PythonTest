import pytest

from src.Exception import (
    MissingArgumentException,
    NoPositiveNumberException,
    Only1ArgumentException,
)
from src.IsPrime import IsPrime


class TestIsPrime:
    """
/*

### ⬜ WHITE-BOX TESTING (Flow & Branch Coverage)

| #   | Flow (Conditions)                            | Condition                          | Input         | Expected Output             |
| --- | -------------------------------------------- | ---------------------------------- | ------------- | --------------------------- |
| 1   | IF-1 (T)                                     | args is None                       | None          | MissingArgumentException    |
| 2   | IF-1 (T)                                     | len(args) == 0                     | []            | MissingArgumentException    |
| 3   | IF-1 (F), IF-2 (T)                           | len(args) > 1                      | [2, 3]        | Only1ArgumentException      |
| 4   | IF-1 (F), IF-2 (F), TRY -> EXCEPT            | float(args[0]) inválido            | ["abc"]       | NoPositiveNumberException   |
| 5   | IF-1 (F), IF-2 (F), TRY, IF-3 (T)            | num <= 0                           | ["0"]         | NoPositiveNumberException   |
| 6   | IF-1 (F), IF-2 (F), TRY, IF-3 (F), IF-4 (T)  | num == 1                           | ["1"]         | False                       |
| 7   | FOR entra, IF-5 (T)                          | num % i == 0 en alguna iteración   | ["4"]         | False                       |
| 8   | FOR entra, IF-5 siempre (F)                  | sin divisores en [2..num-1]        | ["5"]         | True                        |
| 9   | FOR no entra                                 | range(2, num) vacío                | ["2"]         | True                        |

### ⬛ BLACK-BOX TESTING (EP & Boundary Value Analysis)

| #   | Condition / Technique                                   | Input        | Expected Output           |
| --- | ------------------------------------------------------- | ------------ | ------------------------- |
| 1   | BVA: límite negativo cercano a cero                     | ["-0.00001"] | NoPositiveNumberException |
| 2   | BVA: decimal positivo entre 1 y 2 (truncado a 1)        | ["1.9999"]   | False                     |
| 3   | EP: notación científica válida que representa entero    | ["2e0"]      | True                      |

*/
    """

    @pytest.mark.parametrize(
        "args, expected",
        [
            (["1"], False),
            (["4"], False),
            (["5"], True),
            (["2"], True),
            (["1.9999"], False),
            (["2e0"], True),
        ],
    )
    def test_returns_expected_boolean_for_valid_inputs(self, args, expected):
        # Arrange

        # Act
        result = IsPrime.is_prime(args)

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
            (["-0.00001"], NoPositiveNumberException),
        ],
    )
    def test_raises_expected_exception_for_invalid_inputs(self, args, expected_exception):
        # Arrange

        # Act & Assert
        with pytest.raises(expected_exception):
            IsPrime.is_prime(args)

import pytest

from src.Exception import (
    MissingArgumentException,
    NoPositiveNumberException,
    Only1ArgumentException,
)
from src.IsPrime import IsPrime


class TestIsPrime:
    """
    ### WHITE-BOX TESTING (Flow & Branch Coverage)

    | # | Flow (Conditions)                               | Condition                          | Input           | Expected Output             |
    |---|--------------------------------------------------|------------------------------------|-----------------|-----------------------------|
    | 1 | IF-1 (T)                                         | args is None                       | None            | MissingArgumentException    |
    | 2 | IF-1 (F), IF-2 (T)                               | len(args) > 1                      | ["2", "3"]     | Only1ArgumentException      |
    | 3 | IF-1 (F), IF-2 (F), TRY -> CAST ERROR            | ValueError / TypeError             | ["abc"]         | NoPositiveNumberException   |
    | 4 | IF-1 (F), IF-2 (F), TRY -> IF num <= 0 (T)       | num <= 0                           | ["0"]           | NoPositiveNumberException   |
    | 5 | IF-1 (F), IF-2 (F), TRY -> IF num == 1 (T)       | num == 1                           | ["1"]           | False                       |
    | 6 | IF-1 (F), IF-2 (F), TRY -> LOOP finds divisor    | num % i == 0                       | ["4"]           | False                       |
    | 7 | IF-1 (F), IF-2 (F), TRY -> LOOP without divisor  | no divisor in range(2, num)        | ["2"]           | True                        |

    ### BLACK-BOX TESTING (EP & Boundary Value Analysis)

    | # | Condition / Technique                            | Input           | Expected Output |
    |---|--------------------------------------------------|-----------------|-----------------|
    | 1 | EP: Decimal exacto equivalente a entero          | ["3.0"]         | True            |
    | 2 | EP: Decimal positivo no entero (cast truncado)   | ["2.9"]         | True            |
    | 3 | EP: String numérico con espacios                 | [" 7 "]         | True            |
    """

    @pytest.mark.parametrize(
        "args, expected",
        [
            (["1"], False),
            (["4"], False),
            (["2"], True),
            (["3.0"], True),
            (["2.9"], True),
            ([" 7 "], True),
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
            (["2", "3"], Only1ArgumentException),
            (["abc"], NoPositiveNumberException),
            (["0"], NoPositiveNumberException),
        ],
    )
    def test_raises_expected_exception_for_invalid_inputs(self, args, expected_exception):
        # Arrange

        # Act & Assert
        with pytest.raises(expected_exception):
            IsPrime.is_prime(args)

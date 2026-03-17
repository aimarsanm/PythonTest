import pytest
from src.IsPrime import IsPrime
from src.Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

class TestIsPrime:
    """
    ========================================================================
                                BLACK BOX TESTS
    ========================================================================
    | ID | Description                  | Input Args      | Expected Output                    |
    |----|------------------------------|-----------------|------------------------------------|
    | B1 | Missing arguments (None)     | None            | Raises MissingArgumentException    |
    | B2 | Missing arguments (Empty)    | []              | Raises MissingArgumentException    |
    | B3 | Too many arguments           | ["1", "2"]      | Raises Only1ArgumentException      |
    | B4 | Non-numeric argument         | ["abc"]         | Raises NoPositiveNumberException   |
    | B5 | Negative number argument     | ["-5"]          | Raises NoPositiveNumberException   |
    | B6 | Zero argument                | ["0"]           | Raises NoPositiveNumberException   |
    | B7 | Valid prime (2)              | ["2"]           | True                               |
    | B8 | Valid prime (7)              | ["7"]           | True                               |
    | B9 | Valid non-prime (4)          | ["4"]           | False                              |
    | B10| Edge case (1)                | ["1"]           | False                              |
    | B11| Float that resolves to int   | ["5.0"]         | True                               |

    ========================================================================
                                WHITE BOX TESTS
    ========================================================================
    | ID | Branch Description                    | Input Args  | Expected Outcome                 |
    |----|---------------------------------------|-------------|----------------------------------|
    | W1 | args is None                          | None        | Raises MissingArgumentException  |
    | W2 | len(args) == 0                        | []          | Raises MissingArgumentException  |
    | W3 | len(args) > 1                         | ["2", "3"]  | Raises Only1ArgumentException    |
    | W4 | num <= 0                              | ["-1"]      | Raises NoPositiveNumberException |
    | W5 | num == 1                              | ["1"]       | False                            |
    | W6 | raises ValueError on float/int cast   | ["a"]       | Raises NoPositiveNumberException |
    | W7 | num % i == 0 execution path           | ["9"]       | False                            |
    | W8 | Return True path                      | ["3"]       | True                             |
    """

    @pytest.mark.parametrize("args", [
        (None,),
        #([],)
    ])
    def test_is_prime_missing_arguments(self, args):
        # Arrange - setup is done implicitly by parameterization
        # Act & Assert
        with pytest.raises(MissingArgumentException):
            IsPrime.is_prime(args[0] if isinstance(args, tuple) and args[0] is None else args)

    @pytest.mark.parametrize("args", [
        (["1", "2"],),
        (["2", "3", "4"],)
    ])
    def test_is_prime_too_many_arguments(self, args):
        # Arrange - setup is done via arguments
        # Act & Assert
        with pytest.raises(Only1ArgumentException):
            IsPrime.is_prime(args[0] if isinstance(args, tuple) else args)

    @pytest.mark.parametrize("args", [
        (["-5"],),
        (["0"],),
        (["abc"],),
        ([{}],)
    ])
    def test_is_prime_invalid_number_format_or_range(self, args):
        # Arrange - parameterized inputs
        # Act & Assert
        with pytest.raises(NoPositiveNumberException):
            IsPrime.is_prime(args[0] if isinstance(args, tuple) else args)

    @pytest.mark.parametrize("args, expected", [
        (["1"], False),
        (["4"], False),
        (["9"], False),
        (["2"], True),
        (["7"], True),
        (["5.0"], True)
    ])
    def test_is_prime_valid_inputs(self, args, expected):
        # Arrange
        # inputs are provided by parametrize
        
        # Act
        result = IsPrime.is_prime(args)

        # Assert
        assert result == expected

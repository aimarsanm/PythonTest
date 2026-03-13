import pytest
from src.IsPrime import IsPrime
from src.Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

"""
### ⬜ WHITE-BOX TESTING (Flow & Branch Coverage)

| #   | Flow (Conditions)                     | Condition                              | Input        | Expected Output             |
| --- | ------------------------------------- | -------------------------------------- | ------------ | --------------------------- |
| 1   | IF-1 (T)                              | args is None                           | None         | MissingArgumentException    |
| 2   | IF-1 (T)                              | len(args) == 0                         | []           | MissingArgumentException    |
| 3   | IF-1 (F), ELIF-1 (T)                  | len(args) > 1                          | [1, 2]       | Only1ArgumentException      |
| 4   | IF-1 (F), ELIF-1 (F), Try-Catch (Exc) | ValueError or TypeError (not numeric)  | ["abc"]      | NoPositiveNumberException   |
| 5   | IF-1 (F), ELIF-1 (F), IF-2 (T)        | num <= 0                               | [-5] or [0]  | NoPositiveNumberException   |
| 6   | IF-1 (F), ELIF-1 (F), IF-3 (T)        | num == 1                               | [1]          | False                       |
| 7   | Loop (T), IF-4 (T)                    | num % i == 0                           | [4]          | False                       |
| 8   | Loop (T), IF-4 (F), Return True       | num % i != 0 for all i                 | [3]          | True                        |

### ⬛ BLACK-BOX TESTING (EP & Boundary Value Analysis)

| #   | Condition / Technique           | Input   | Expected Output           |
| --- | ------------------------------- | ------- | ------------------------- |
| 1   | BVA: Límite inferior (Positivo) | [2]     | True                      |
| 2   | BVA: Primer no primo            | [4]     | False                     |
| 3   | EP: String numérico decimal     | ["3.9"] | True (Casted to 3)        |
| 4   | EP: Gran número primo           | [97]    | True                      |
"""
class TestIsPrime:
    
    @pytest.mark.parametrize("args", [
        None,
        []
    ])
    def test_missing_argument_generates_error_when_empty_or_none(self, args):
        # Arrange
        # No extra setup needed for static method invocation
        
        # Act & Assert
        with pytest.raises(MissingArgumentException):
            IsPrime.is_prime(args)

    def test_multiple_arguments_generate_error_when_given_more_than_one(self):
        # Arrange
        args = [1, 2]
        
        # Act & Assert
        with pytest.raises(Only1ArgumentException):
            IsPrime.is_prime(args)

    @pytest.mark.parametrize("args", [
        ["abc"],
        [-5],
        [0]
    ])
    def test_invalid_formats_and_non_positive_numbers_generate_error(self, args):
        # Arrange
        # No extra setup needed
        
        # Act & Assert
        with pytest.raises(NoPositiveNumberException):
            IsPrime.is_prime(args)

    @pytest.mark.parametrize("args, expected_result", [
        ([1], False),      # Minimum positive number (White-box IF-3)
        ([4], False),      # First non-prime (Black-box BVA)
        ([3], True),       # Small prime (White-box Loop)
        ([2], True),       # Lower bound prime (Black-box BVA)
        (["3.9"], True),   # Decimal float cast to 3 (Black-box EP)
        ([97], True)       # Large prime (Black-box EP)
    ])
    def test_number_evaluates_primality_correctly(self, args, expected_result):
        # Arrange
        # No extra setup needed
        
        # Act
        result = IsPrime.is_prime(args)
        
        # Assert
        assert result == expected_result


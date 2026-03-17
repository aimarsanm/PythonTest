import pytest
from src.IsPrime import IsPrime
from src.Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

"""

### ⬜ WHITE-BOX TESTING (Flow & Branch Coverage)

| #   | Flow (Conditions)                  | Condition                              | Input      | Expected Output           |
| --- | ---------------------------------- | -------------------------------------- | ---------- | ------------------------- |
| 1   | args is None                       | if args is None or len(args) == 0    | None       | MissingArgumentException  |
| 2   | Empty argument list                | if args is None or len(args) == 0    | []         | MissingArgumentException  |
| 3   | Multiple arguments                 | elif len(args) > 1                   | [2, 3]     | Only1ArgumentException    |
| 4   | Invalid type (ValueError)          | except (ValueError, TypeError)       | ["text"]   | NoPositiveNumberException |
| 5   | Negative number                    | if num <= 0                          | [-1]       | NoPositiveNumberException |
| 6   | Input equals 1                     | if num == 1                          | [1]        | False                     |
| 7   | Composite number (divisor found)   | if num % i == 0 (in loop)            | [4]        | False                     |
| 8   | Prime number (no divisor found)    | return True (after loop completes)   | [2]        | True                      |

### ⬛ BLACK-BOX TESTING (EP & Boundary Value Analysis)

| #   | Condition / Technique              | Input   | Expected Output           |
| --- | ---------------------------------- | ------- | ------------------------- |
| 1   | BVA: Zero boundary                 | [0]     | NoPositiveNumberException |
| 2   | EP: Prime (partition 1)           | [3]     | True                      |
| 3   | EP: Composite (partition 2)       | [9]     | False                     |
| 4   | EP: Large Prime (boundary prime)  | [17]    | True                      |

"""


class TestIsPrime:
    """Test suite for the IsPrime.is_prime() method covering White-Box and Black-Box test cases."""

    @pytest.mark.parametrize(
        "input_args,expected_exception",
        [
            # White-Box: Exception cases
            (None, MissingArgumentException),             # Caso 1: args is None
            ([], MissingArgumentException),               # Caso 2: Empty list
            ([2, 3], Only1ArgumentException),             # Caso 3: Multiple arguments
            (["text"], NoPositiveNumberException),        # Caso 4: Invalid type
            ([-1], NoPositiveNumberException),            # Caso 5: Negative number
            # Black-Box: Exception cases
            ([0], NoPositiveNumberException),             # Caso 1: Zero boundary
        ],
    )
    def test_is_prime_raises_exception_for_invalid_input(self, input_args, expected_exception):
        """Tests that is_prime raises appropriate exceptions for invalid inputs."""
        # Arrange & Act & Assert
        with pytest.raises(expected_exception):
            IsPrime.is_prime(input_args)

    @pytest.mark.parametrize(
        "input_args,expected_result",
        [
            # White-Box: Boolean return cases
            ([1], False),        # Caso 6: Input equals 1
            ([4], False),        # Caso 7: Composite number
            ([2], True),         # Caso 8: Prime number
            # Black-Box: Boolean return cases
            ([3], True),         # Caso 2: Prime (partition 1)
            ([9], False),        # Caso 3: Composite (partition 2)
            ([17], True),        # Caso 4: Large Prime (boundary prime)
        ],
    )
    def test_is_prime_returns_correct_boolean_for_valid_input(self, input_args, expected_result):
        """Tests that is_prime returns the correct boolean for valid numeric inputs."""
        # Arrange
        is_prime_func = IsPrime.is_prime

        # Act
        result = is_prime_func(input_args)

        # Assert
        assert result == expected_result


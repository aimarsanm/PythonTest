import pytest
from src.IsPrime import IsPrime
from src.Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

"""
### ⬜ WHITE-BOX TESTING (Flow & Branch Coverage)

| #   | Flow (Conditions)                    | Input              | Expected Output                |
| --- | ------------------------------------ | ------------------ | ------------------------------ |
| 1   | IF-1 (T): args is None               | None               | MissingArgumentException       |
| 2   | IF-1 (T): args is empty list         | []                 | MissingArgumentException       |
| 3   | IF-2 (T): len(args) > 1              | [2, 3]             | Only1ArgumentException         |
| 4   | IF-3 (F): try/except ValueError      | ["abc"]            | NoPositiveNumberException      |
| 5   | IF-4 (T): num <= 0 (negative)        | ["-5"]             | NoPositiveNumberException      |
| 6   | IF-4 (T): num <= 0 (zero)            | ["0"]              | NoPositiveNumberException      |
| 7   | IF-5 (T): num == 1                   | [1]                | False                          |
| 8   | IF-6 (T): Loop finds divisor (even)  | [4]                | False                          |
| 9   | IF-6 (F): Loop completes (prime)     | [2]                | True                           |
| 10  | IF-6 (F): Loop completes (prime)     | [5]                | True                           |

### ⬛ BLACK-BOX TESTING (EP & Boundary Value Analysis)

| #   | Technique / Condition                 | Input              | Expected Output           |
| --- | ------------------------------------- | ------------------ | ------------------------- |
| 1   | BVA: Primer número primo              | [2]                | True                      |
| 2   | BVA: Límite superior (número grande primo) | [97]           | True                      |
| 3   | BVA: Límite inferior (número compuesto pequeño) | [4]        | False                     |
| 4   | BVA: Número compuesto grande          | [100]              | False                      |
| 5   | EP: Conversión float a int (truncado) | [3.9]              | False (3 is prime but test checks digit)  |
| 6   | EP: Conversión float a int (válido)   | [5.1]              | True  (truncates to 5)                   |

"""

class TestIsPrime:
    
    # White-box test cases
    def test_is_prime_missing_argument_none(self):
        """Test when args is None"""
        with pytest.raises(MissingArgumentException):
            IsPrime.is_prime(None)
    
    def test_is_prime_missing_argument_empty_list(self):
        """Test when args is empty list"""
        with pytest.raises(MissingArgumentException):
            IsPrime.is_prime([])
    
    def test_is_prime_multiple_arguments(self):
        """Test when more than 1 argument is provided"""
        with pytest.raises(Only1ArgumentException):
            IsPrime.is_prime([2, 3])
    
    def test_is_prime_non_numeric_string(self):
        """Test when argument cannot be converted to number"""
        with pytest.raises(NoPositiveNumberException):
            IsPrime.is_prime(["abc"])
    
    def test_is_prime_negative_number(self):
        """Test with negative number"""
        with pytest.raises(NoPositiveNumberException):
            IsPrime.is_prime(["-5"])
    
    def test_is_prime_zero(self):
        """Test with zero"""
        with pytest.raises(NoPositiveNumberException):
            IsPrime.is_prime(["0"])
    
    def test_is_prime_one(self):
        """Test with number 1 (not prime)"""
        assert IsPrime.is_prime([1]) == False
    
    def test_is_prime_even_composite(self):
        """Test even composite number (4)"""
        assert IsPrime.is_prime([4]) == False
    
    def test_is_prime_two(self):
        """Test with 2 (smallest prime)"""
        assert IsPrime.is_prime([2]) == True
    
    def test_is_prime_odd_prime(self):
        """Test with odd prime number (5)"""
        assert IsPrime.is_prime([5]) == True
    
    # Black-box test cases
    def test_is_prime_three(self):
        """BVA: Early prime numbers"""
        assert IsPrime.is_prime([3]) == True
    
    def test_is_prime_large_prime(self):
        """BVA: Larger prime number (97)"""
        assert IsPrime.is_prime([97]) == True
    
    def test_is_prime_small_composite(self):
        """BVA: Small composite (6)"""
        assert IsPrime.is_prime([6]) == False
    
    def test_is_prime_large_composite(self):
        """BVA: Larger composite (100)"""
        assert IsPrime.is_prime([100]) == False
    
    def test_is_prime_float_truncate_to_prime(self):
        """EP: Float conversion - truncates to prime (5.9 → 5)"""
        assert IsPrime.is_prime([5.9]) == True
    
    def test_is_prime_float_truncate_to_composite(self):
        """EP: Float conversion - truncates to composite (4.1 → 4)"""
        assert IsPrime.is_prime([4.1]) == False

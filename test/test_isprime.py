import pytest
import sys
sys.path.insert(0, '../src')

from isPrime import is_prime
from Exception import MissingArgumentException, Only1ArgumentException, NoPositiveNumberException

"""

### ⬜ WHITE-BOX TESTING (Flow & Branch Coverage)

| #   | Flow (Conditions)                      | Input           | Expected Output           |
| --- | -------------------------------------- | --------------- | ------------------------- |
| 1   | IF-1 (T): args is None                 | None            | MissingArgumentException  |
| 2   | IF-1 (T): len(args) == 0               | []              | MissingArgumentException  |
| 3   | ELIF-1 (T): len(args) > 1              | [2, 3]          | Only1ArgumentException    |
| 4   | ELSE → IF-2 (T): num <= 0              | [0]             | NoPositiveNumberException |
| 5   | ELSE → IF-2 (T): num <= 0 (negative)   | [-5]            | NoPositiveNumberException |
| 6   | ELSE → IF-3 (T): num == 1              | [1]             | False                     |
| 7   | ELSE → FOR (T): divisor found          | [4]             | False                     |
| 8   | ELSE → FOR (F): no divisor found       | [2]             | True                      |
| 9   | ELSE → EXCEPT (ValueError/TypeError)   | ["abc"]         | NoPositiveNumberException |
| 10  | ELSE → FOR (no iterations): num == 2   | [2]             | True                      |

### ⬛ BLACK-BOX TESTING (EP & Boundary Value Analysis)

| #   | Condition / Technique                  | Input           | Expected Output           |
| --- | -------------------------------------- | --------------- | ------------------------- |
| 1   | BVA: Límite inferior válido (2)        | [2]             | True                      |
| 2   | EP: Número primo pequeño               | [3]             | True                      |
| 3   | EP: Número primo grande                | [97]            | True                      |
| 4   | BVA: Límite entre no-primo y primo     | [4]             | False                     |
| 5   | EP: Número compuesto (múltiplo de 2)   | [10]            | False                     |
| 6   | BVA: Decimal válido → entero primo     | [2.7]           | True                      |
| 7   | BVA: Decimal válido → entero no primo  | [4.9]           | False                     |

"""


class TestIsPrime:
    
    # WHITE-BOX Test Cases
    
    def test_whitebox_1_args_is_none(self):
        """IF-1 (T): args is None"""
        with pytest.raises(MissingArgumentException):
            is_prime(None)
    
    def test_whitebox_2_empty_args(self):
        """IF-1 (T): len(args) == 0"""
        with pytest.raises(MissingArgumentException):
            is_prime([])
    
    def test_whitebox_3_multiple_args(self):
        """ELIF-1 (T): len(args) > 1"""
        with pytest.raises(Only1ArgumentException):
            is_prime([2, 3])
    
    def test_whitebox_4_zero_input(self):
        """ELSE → IF-2 (T): num == 0"""
        with pytest.raises(NoPositiveNumberException):
            is_prime([0])
    
    def test_whitebox_5_negative_input(self):
        """ELSE → IF-2 (T): num < 0"""
        with pytest.raises(NoPositiveNumberException):
            is_prime([-5])
    
    def test_whitebox_6_num_equals_one(self):
        """ELSE → IF-3 (T): num == 1"""
        assert is_prime([1]) is False
    
    def test_whitebox_7_even_number(self):
        """ELSE → FOR (T): divisor found (4 % 2 == 0)"""
        assert is_prime([4]) is False
    
    def test_whitebox_8_prime_number_two(self):
        """ELSE → FOR (F): no divisor found (range(2, 2) empty)"""
        assert is_prime([2]) is True
    
    def test_whitebox_9_invalid_string(self):
        """ELSE → EXCEPT (ValueError/TypeError): "abc" cannot convert"""
        with pytest.raises(NoPositiveNumberException):
            is_prime(["abc"])
    
    def test_whitebox_10_prime_number_three(self):
        """ELSE → FOR (F): no divisor found for 3"""
        assert is_prime([3]) is True
    
    # BLACK-BOX Test Cases
    
    def test_blackbox_1_bva_smallest_prime(self):
        """BVA: Límite inferior válido (2 - smallest prime)"""
        assert is_prime([2]) is True
    
    def test_blackbox_2_ep_small_prime(self):
        """EP: Número primo pequeño"""
        assert is_prime([3]) is True
    
    def test_blackbox_3_ep_large_prime(self):
        """EP: Número primo grande"""
        assert is_prime([97]) is True
    
    def test_blackbox_4_bva_non_prime_boundary(self):
        """BVA: Límite entre no-primo y primo"""
        assert is_prime([4]) is False
    
    def test_blackbox_5_ep_composite_even(self):
        """EP: Número compuesto (múltiplo de 2)"""
        assert is_prime([10]) is False
    
    def test_blackbox_6_bva_decimal_to_prime(self):
        """BVA: Decimal válido → entero primo (2.7 → 2)"""
        assert is_prime([2.7]) is True
    
    def test_blackbox_7_bva_decimal_to_non_prime(self):
        """BVA: Decimal válido → entero no primo (4.9 → 4)"""
        assert is_prime([4.9]) is False

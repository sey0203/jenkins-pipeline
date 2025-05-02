import pytest

def add(a: int, b: int) -> int:
    """두 숫자를 더하는 함수입니다."""
    return a + b

class TestAdd:
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5, "2 + 3은 5여야 합니다."
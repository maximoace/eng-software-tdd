import pytest
from .two import SizeError, difference_of_diagonals

class TestClass():
    
    def test_true_one(self):
        matrix = [[1,2,3], [4,5,6], [9,8,9]]
        assert difference_of_diagonals(matrix) == 2

    def test_true_two(self):
        matrix = [[3,5,35], [7,10,12], [1,9,20]]
        assert difference_of_diagonals(matrix) == 13

    def test_negative_numbers(self):
        matrix = [[-10,-20, -6], [-15,-7,-17], [-9, -13, -3]]
        assert difference_of_diagonals(matrix) == 2

    def test_too_small(self):
        matrix = [2]
        with pytest.raises(SizeError):
            assert difference_of_diagonals(matrix)

    def test_too_large(self):
        line =[x for x in range(1001)]
        matrix = [line for _ in range(1001)]
        with pytest.raises(SizeError):
            assert difference_of_diagonals(matrix)

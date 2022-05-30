import pytest
from .one import SizeError, sum_of_array

class TestClass():

    def test_simple(self):
        assert sum_of_array([1,2,3]) == 6

    def test_negative(self):
        assert sum_of_array([-5,-6,-4]) == -15

    def test_string(self):
        with pytest.raises(TypeError):
            assert sum_of_array(['A', 1, 2]) == 67 # 'A' ASCII value = 65

    def test_too_small(self):
        with pytest.raises(SizeError):
            assert sum_of_array([]) == None

    def test_too_large(self):
        with pytest.raises(SizeError):

            aux_list = list()
            for i in range(1010):
                aux_list.append(1)
            
            assert sum_of_array(aux_list) == 1010
from .three import is_palindrome

class TestClass():

    def test_true_one (self):
        assert is_palindrome('ovo')

    def test_true_two (self):
        assert is_palindrome('ABBA')

    def test_true_three (self):
        assert is_palindrome('socorram me subi no onibus em marrocos')

    def test_false (self):
        assert not is_palindrome('não é palindromo')

    def test_capitalized (self):
        assert is_palindrome('Abcdcba')
from Alternating_Characters.alter_code import alternatingCharacters
import unittest

class alter_test(unittest.TestCase):
    def test_AAABBBAABB(self):
        input = "AAABBBAABB"
        test = alternatingCharacters(input)
        self.assertIs(test,6)

    def test_1234556678(self):
        input = "1234556678"
        test = alternatingCharacters(input)
        self.assertIs(test,2)

    def test_sa_dd(self):
        input = "sa_dd"
        test = alternatingCharacters(input)
        self.assertIs(test,1)

    def test_1add1add1add1(self):
        input = "1@1@1@1"
        test = alternatingCharacters(input)
        self.assertIs(test,0)

    
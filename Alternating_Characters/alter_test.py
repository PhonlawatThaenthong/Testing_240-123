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
    
    def test_longtext(self):
        input = '''AABBABABBBBBABBABABBBBABBABABABBABBABBBBAAABBBBBBBBBBBABBBBBBBABBBBBBBBBBBBABBABBBBAABBBBBAAAABBBBBB'''
        test = alternatingCharacters(input)
        self.assertIs(test,62)

    def test_extra(self):
        input = "#@$()****"
        test = alternatingCharacters(input)
        self.assertIs(test,3)
    
    def test_number_with_text(self):
        input = "dsadsd123123"
        test = alternatingCharacters(input)
        self.assertIs(test,0)

    def test_samenumber(self):
        input = "11111111111111"
        test = alternatingCharacters(input)
        self.assertIs(test,13)
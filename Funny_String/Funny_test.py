from Funny_String.Funny_string import funnyString
import unittest

class Test_Funny(unittest.TestCase):
    def test_acxz(self):
        input = 'acxz'
        test = funnyString(input)
        self.assertEqual('Funny',test)

    def test_bcxz(self):
        input = 'bcxz'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_ivvkxq(self):
        input = 'ivvkxq'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_extra(self):
        input = '@#&*$'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_ivvkx(self):
        input = 'ivvkx'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)

    def test_longtext(self):
        input = 'djaddsadssadajdasdasjdhuxyxycxhwnqndbasvcxzdadasdsadcxzgtuysawdsa'
        test = funnyString(input)
        self.assertEqual('Not Funny',test)
    
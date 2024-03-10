from Grid_challenge.grid_challenge import gridChallenge
import unittest
from mock import patch

class Two_character(unittest.TestCase):
    def test_1(self):
        input = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        test = gridChallenge(input)
        self.assertEqual('YES',test)
    
    def test_2(self):
        input = ['311','222','133']
        test = gridChallenge(input)
        self.assertEqual('NO',test)

    def test_3(self):
        input = ['#','@','$','%']
        test = gridChallenge(input)
        self.assertEqual('NO',test)

    def test_4(self):
        input = ['7']
        test = gridChallenge(input)
        self.assertEqual('YES',test)

    def test_5(self):
        input = ['abc','hjk','mpq','rtv']
        test = gridChallenge(input)
        self.assertEqual('YES',test)

    def test_6(self):
        input = ['uxf','vof','hmp']
        test = gridChallenge(input)
        self.assertEqual('NO',test)
    
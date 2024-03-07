from Two_Character.two_character import alternate
import unittest

class Two_character(unittest.TestCase):
    def test_beabeefeab(self):
        input = 'beabeefeab'
        test = alternate(input)
        self.assertEqual(5,test)

    def test_asdcbsdcagfsdbgdfanfghbsfdab(self):
        input = 'asdcbsdcagfsdbgdfanfghbsfdab'
        test = alternate(input)
        self.assertEqual(8,test)

    def test_asvkugfiugsalddlasguifgukvsa(self):
        input = 'asvkugfiugsalddlasguifgukvsa'
        test = alternate(input)
        self.assertEqual(0,test)
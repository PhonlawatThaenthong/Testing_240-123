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

    def test_extra(self):
        input = '###########'
        test = alternate(input)
        self.assertEqual(0,test)

    def test_space(self):
        input = ''
        test = alternate(input)
        self.assertEqual(0,test)

    def test_longspace(self):
        input = '           '
        test = alternate(input)
        self.assertEqual(0,test)

    def test_number(self):
        input = '321313123'
        test = alternate(input)
        self.assertEqual(7,test)
    
    def test_text_and_space(self):
        input = 'a e i o u'
        test = alternate(input)
        self.assertEqual(2,test)

    def test_text_and_extra(self):
        input = 'a#u&i@x$p'
        test = alternate(input)
        self.assertEqual(2,test)

    def test_samenumber(self):
        input = '222222222'
        test = alternate(input)
        self.assertEqual(0,test)
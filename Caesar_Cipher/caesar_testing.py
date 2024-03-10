from Caesar_Cipher.caesar_cipher import caesarCipher
import unittest

class Caesar_Testing(unittest.TestCase):
    def test_middle_Outz(self):
        input = 'middle-Outz'
        number = 2
        test = caesarCipher(input,number)
        self.assertEqual('okffng-Qwvb',test)

    def test_Always_Look_on_the_Bright_Side_of_Life(self):
        input = 'Always-Look-on-the-Bright-Side-of-Life'
        number = 5
        test = caesarCipher(input,number)
        self.assertEqual('Fqbfdx-Qttp-ts-ymj-Gwnlmy-Xnij-tk-Qnkj',test)

    def test_AAAA(self):
        input = 'AAAA'
        number = 6
        test = caesarCipher(input,number)
        self.assertEqual('GGGG',test)
    
    def test_mark(self):
        input = 'mark'
        number = 26
        test = caesarCipher(input,number)
        self.assertEqual('mark',test)
    
    def test_extra(self):
        input = '%@#$'
        number = 2
        test = caesarCipher(input,number)
        self.assertEqual('%@#$',test)

    def test_number(self):
        input = '3123212'
        number = 21
        test = caesarCipher(input,number)
        self.assertEqual('3123212',test)
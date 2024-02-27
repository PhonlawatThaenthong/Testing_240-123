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

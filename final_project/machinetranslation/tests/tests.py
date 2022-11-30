import unittest
from translator import english_to_french, french_to_english

class testTranslator(unittest.TestCase):
    def test_null_englishToFrench(self):
        self.assertEqual(english_to_french(''), '')
    def test_null_frenchToEnglish(self):
        self.assertEqual(french_to_english(''), '')
    def test_hello_englishToFrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    def test_bonjour_frenchToEnglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
unittest.main()
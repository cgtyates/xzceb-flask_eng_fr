import unittest
import translator

class TestTranslator(unittest.TestCase):
    def test1(self):
        self.assertEqual(translator.englishToFrench('Hello'),'Bonjour')
        self.assertEqual(translator.englishToFrench(''),'')

    def test2(self):
        self.assertEqual(translator.frenchToEnglish('Bonjour'),'Hello')
        self.assertEqual(translator.frenchToEnglish(''),'')

if __name__ == '__main__':
    unittest.main()
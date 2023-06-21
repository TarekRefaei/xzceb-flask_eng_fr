import unittest
from translator import englishToFrench , frenchtoEnglish

class translatorTest (unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench("Hello"),"Bonjour")
    
    def test2(self):
        self.assertEqual(frenchtoEnglish("Bonjour"),"Hello")

unittest.main()
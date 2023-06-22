import unittest
from translator import english_to_french , french_to_english

class translatorTest (unittest.TestCase):
    def test1(self) :
        self.assertEqual(english_to_french("Good morning"),"Bonjour")
    
    def test2(self) :
        self.assertEqual(french_to_english("Bonjour"),"Hello")

unittest.main()
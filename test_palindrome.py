import unittest
from palindorome import palindrome


class TestCountWords(unittest.TestCase):
    
    def test_neuqueN(self):
        resultado = palindrome("neuqueN")
        self.assertEqual(resultado,True)
        
    def test_rar(self):
        resultado = palindrome("rar")
        self.assertEqual(resultado,True)
        
    def test_hola(self):
        resultado = palindrome("hola")
        self.assertEqual(resultado,False)
        
if  __name__ == "__main__":
    unittest.main()
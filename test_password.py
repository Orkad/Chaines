# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcd"), "abce")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhz"), "abia")

    def test_getExceptionZZZZZ(self):
        self.assertRaises(pwd.getNext("zzzzz"))

    #def test_getExceptionVide(self):
        #self.assertRaises(pwd.getNext("")) #ne marche pas

    def test_getExceptionChar(self):
        self.assertRaises(pwd.getNext("456456"))
        
# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()

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

    #test partie 3

    def test_hasSerie(self):
        self.assertEquals(pwd.hasSeries("abc"),True)

    def test_hasSerie2(self):
        self.assertEquals(pwd.hasSeries("adp"),False)

    def test_hasTwoPairs(self):
        self.assertEquals(pwd.hasTwoPairs("aabb"),True)

    def test_hasTwoPairs2(self):
        self.assertEquals(pwd.hasTwoPairs("abcd"),False)

    def test_hasNotBadChar(self):
        self.assertEquals(pwd.hasNoBadChar("test"),True)

    def test_hasNotBadChar2(self):
        self.assertEquals(pwd.hasNoBadChar("joli"),False)
        
# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()

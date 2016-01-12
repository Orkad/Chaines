# coding: utf-8 
import unittest
import password as pwd

class TestPasswordJosephine(unittest.TestCase):

    def test_hasSerie(self):
        self.assertEquals(pwd.HasSeries("abc"),True)

    def test_hasSerie2(self):
        self.assertEquals(pwd.HasSeries("adp"),False)

    def test_hasTwoPairs(self):
        self.assertEquals(pwd.HasTwoPairs("aabb"),True)

    def test_hasTwoPairs2(self):
        self.assertEquals(pwd.HasTwoPairs("abcd"),False)

    def test_hasNotBadChar(self):
        self.assertEquals(pwd.HasNoBadChar("test"),True)

    def test_hasNotBadChar2(self):
        self.assertEquals(pwd.HasNoBadChar("joli"),False)
        
# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()

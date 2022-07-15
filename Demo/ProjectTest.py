#!/usr/bin/env python
# coding: utf-8

import unittest
from dieclass import Die
from gameclass import Game
from analyzerclass import Analyzer

class ProjectTestSuite(unittest.TestCase):
    
    def test_1_change_w(self):
        """
        Tests change_w method
        """
        test_object=Die([1,2,3,4,4])
        test_object.change_w(4, 0.8)
        self.assertTrue(((test_object._diedf['faces'] == 4) & ((test_object._diedf['weights']== 0.8))).any())
                        
    def test_2_rolldice(self):
        """
        Tests rolldice method
        """
        test_object=Die([1,2,3,4,4])
        test_object.rolldie(5)
        self.assertTrue(len(test_object.rolldie(5)) == 5)
        
    def test_3_display(self):
        """
        Tests display method
        """
        test_object=Die([1,2,3,4,4])
        test_object.display()
        self.assertTrue(test_object._diedf.shape[0] != 0)
        
    def test_4_play(self):
        """
        Tests play method
        """
        die1=Die([2,3,4])
        die2=Die([1,2,3])
        test_object=Game([die1,die2])
        test_object.play(22)
        self.assertTrue(len(test_object._rolldf) == 22)
    
    def test_5_show(self):
        """
        Tests show method with form as wide
        """
        die1=Die([2,3,4])
        die2=Die([1,2,3])
        test_object=Game([die1,die2])
        test_object.play(22)
        test_object.show()
        self.assertTrue(test_object._rolldf.shape == (22,2))
        
        
    def test_6_show(self):
        """
        Tests show method with form as narrow
        """
        die1=Die([2,3,4])
        die2=Die([1,2,3])
        test_object=Game([die1,die2])
        test_object.play(22)
        x1 = test_object.show(form = 'narrow')
        self.assertEqual((len(x1)) ,44)
     
    
    def test_7_show(self):
        """
        Tests show method exception raised from incorrect input for form argument. 
        """
        die1=Die([2,3,4])
        die2=Die([1,2,3])
        test_object=Game([die1,die2])
        test_object.play(22)     
        with self.assertRaises(Exception):
            test_object.show(form = 'b')
        
    def test_8_jackpot(self):
        """
        Tests jackpot method
        """
        die1=Die([3,3,3])
        die2=Die([1,3,3])
        game1=Game([die1,die2])
        game1.play(10)
        test_object=Analyzer(game1)
        test_object.jackpot()
        self.assertTrue(len(game1._rolldf) > len(test_object.jackresultdf))
        
    def test_9_combo(self):
        """
        Tests combo method
        """
        die1=Die([3,3,3])
        die2=Die([2,2,2])
        game1=Game([die1,die2])
        game1.play(10)
        test_object=Analyzer(game1)
        test_object.combo()
        self.assertTrue((test_object.uni['Counts']==10).all())
        
        
    def test_10_facecount(self):
        """
        Tests facecount method
        """
        die1=Die([3,3,3])
        die2=Die([2,2,2])
        game1=Game([die1,die2])
        game1.play(1)
        test_object=Analyzer(game1)
        self.assertTrue((test_object.facecount().iloc[0] == 1).all())      

        
if __name__ == '__main__':
    unittest.main(verbosity=2)







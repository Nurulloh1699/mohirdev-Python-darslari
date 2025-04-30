# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 21:05:30 2025

@author: DavrServis
"""
import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(5), 78.53975)
        self.assertAlmostEqual(getArea(10), 314.159)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(4), 23.13272)
        self.assertAlmostEqual(getPerimeter(15), 94.2477)
        
unittest.main()

# Natija: Ran 1 test in 0.001s

        # OK
        
# Ikkinchi testimizni natijasini ko'ramiz:
# Natija: Ran 2 tests in 0.002s

        # OK
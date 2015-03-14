#Unit testing 

from MonteCarloSimulationOfPi import MonteCarloSimulationOfPi
import unittest

class TestFunctions(unittest.TestCase):

    def test_small_negative_whole_number(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.estPi(-12345,-98765))

    def test_small_negative_decimal_number(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.estPi(-0.12345,-0.98765))
                        
    def test_zero_number(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.estPi(0,0))

    def test_decimal(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.estPi(1234, 0.456))

if __name__ == '__main__':
    unittest.main()

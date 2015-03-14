#Unit testing

from MonteCarloSimulationOfPi import MonteCarloSimulationOfPi
import unittest

class TestFunctions(unittest.TestCase):

    def test_negative_large(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-245245))

    def test_negative_small(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-7))

    def test_negative_one(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-1))

    def test_zero(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(0))

    def test_positive_one(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(1))

    def test_negative_decimal(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(-5.540))

    def test_positive_decimal(self):
        simulate = PiSimulation()
        self.assertRaises(AssertionError, lambda: simulate.throwNeedles(8.4484))

if __name__ == '__main__':
    unittest.main()

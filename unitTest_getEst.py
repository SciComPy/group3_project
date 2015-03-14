#Unit testing

from MonteCarloSimulationOfPi import MonteCarloSimulationOfPi
import unittest

class TestFunctions(unittest.TestCase):

    def test_negative_large_first(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-223160, 222323))

    def test_negative_large_second(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(223160, -222323))

    def test_negative_small_first(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-1, 4))

    def test_negative_small_second(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(1, -4))

    def test_negative_one_first(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-1, 2))

    def test_negative_one_second(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(2, -1))

    def test_zero_both(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(0,0))

    def test_zero_first(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(0,3))

    def test_zero_second(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(10,0))

    def test_negative_decimal_first(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-4.13321, 1.56562))

    def test_negative_decimal_second(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(4.13321, -1.56562))

    def test_positve_decimal_both(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(4.13321, 1.56562))

    def test_positive_decimal_first(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(4.13321, -1.56562))

    def test_positive_decimal_second(self):
        simulate = MonteCarloSimulationOfPi()
        self.assertRaises(AssertionError, lambda: simulate.getEst(-4.13321, 1.56562))

if __name__ == '__main__':
   unittest.main()

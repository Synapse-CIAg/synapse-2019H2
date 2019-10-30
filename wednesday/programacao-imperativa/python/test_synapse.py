import unittest
from synapse import fatorial, fibonacci, check_prime

class FatorialTest(unittest.TestCase):

    def test_fatorial_1(self):
        result = fatorial(1)
        expected = 1
        self.assertEqual(result, expected)

    def test_fatorial_5(self):
        result = fatorial(5)
        expected = 120
        self.assertEqual(result, expected)

class FibonacciTets(unittest.TestCase):

    def test_fibonacci_0(self):
        result = fibonacci(0)
        expected = 0
        self.assertEqual(result, expected)

    def test_fibonacci_1(self):
        result = fibonacci(1)
        expected = 1
        self.assertEqual(result, expected)

    def test_fibonacci_2(self):
        result = fibonacci(2)
        expected = 1
        self.assertEqual(result, expected)
    
    def test_fibonacci_3(self):
        result = fibonacci(3)
        expected = 2
        self.assertEqual(result, expected)

    def test_fibonacci_6(self):
        result = fibonacci(6)
        expected = 8
        self.assertEqual(result, expected)

class PrimoTest(unittest.TestCase):


    def test_check_1(self):
        result = check_prime(1)
        self.assertFalse(result)

    def test_check_2(self):
        result = check_prime(2)
        self.assertTrue(result)

    def test_check_3(self):
        result = check_prime(3)
        self.assertTrue(result)

    def test_check_9(self):
        result = check_prime(9)
        self.assertFalse(result)

    def test_check_11(self):
        result = check_prime(11)
        self.assertTrue(result)
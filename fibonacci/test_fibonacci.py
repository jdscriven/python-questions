import unittest
import sys
from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_first_few(self):
        """Test the first few elements of the fibonacci sequence,
           using hard coded values."""
        fibs = fibonacci()

        self.assertEqual(0, next(fibs))
        self.assertEqual(1, next(fibs))
        self.assertEqual(1, next(fibs))
        self.assertEqual(2, next(fibs))
        self.assertEqual(3, next(fibs))
        self.assertEqual(5, next(fibs))
        self.assertEqual(8, next(fibs))

    def test_1000_elements(self):
        """Test elements 2-1002, by comparing them with the previous 2."""
        fibs = fibonacci()

        a = next(fibs)
        b = next(fibs)
        for _ in range(1000):
            c = next(fibs)
            self.assertEqual(c, a+b)
            a, b = b, c

    def test_maxsize_limit(self):
        """Request a sequence with sys.maxsize limit number of elements."""
        fibs = fibonacci(sys.maxsize)
        self.assertEqual(0, next(fibs))

    def test_exceed_maxsize_limit(self):
        """Request a sequence with sys.maxsize +1 limit number of elements."""
        self.assertRaises(ValueError, fibonacci, sys.maxsize+1)

    def test_negative_limit(self):
        """Request a sequence with a negative limit number of elements."""
        self.assertRaises(ValueError, fibonacci, -1)

    def test_zero_limit(self):
        """Request a sequence with a zero limit number of elements."""
        # getting empty generator is fine
        fibs = fibonacci(0)
        # but attempt to get any elements will fail
        self.assertRaises(StopIteration, next, fibs)

    def test_one_limit(self):
        """Request a sequence with a limit of one element.
           Ensure the generator is exhausted after reading that element."""
        fibs = fibonacci(1)
        # first next() call ok
        next(fibs)
        # second next() call should fail
        self.assertRaises(StopIteration, next, fibs)

    def test_one_limit_keyword(self):
        """Request a sequence with a limit of one element
           (using a keyword argument).
           Ensure the generator is exhausted after reading that element."""
        fibs = fibonacci(limit=1)
        # first next() call ok
        next(fibs)
        # second next() call should fail
        self.assertRaises(StopIteration, next, fibs)

def main():
    unittest.main()

if __name__ == '__main__':
    main()

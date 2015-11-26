import unittest
from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def testFirstFew(self):
        fibs = fibonacci()

        self.assertEqual(0,next(fibs))
        self.assertEqual(1,next(fibs))
        self.assertEqual(1,next(fibs))
        self.assertEqual(2,next(fibs))
        self.assertEqual(3,next(fibs))
        self.assertEqual(5,next(fibs))
        self.assertEqual(8,next(fibs))

def main():
    unittest.main()

if __name__ == '__main__':
    main()


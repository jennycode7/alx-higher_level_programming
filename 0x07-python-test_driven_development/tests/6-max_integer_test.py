import unittest
max_integer = __import__('6-max_integer').max_integer


class Test_Case(unittest.TestCase):
    """
    A test case
    """
    def test_max_integer(self):
        """
        test for max_integer function
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)
        self.assertEqual(max_integer([-1, -3, -2, -4, -5]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-1]), -1)


if __name__ == "__main__":
    unittest.main()

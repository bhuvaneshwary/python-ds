import unittest
import linkedList

class test_function(unittest.TestCase):
    def test_sum (self):
        self.assertEqual(add(4,5),9)
        self.assertNotEqual(add(6,7),12)
if __name__ == '__main__':
    unittest.main()
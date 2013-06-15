import unittest

from bubble import swap

class MyBubbleSortTest(unittest.TestCase):
    def setUp(self):
       #self.arr = [1, 9, 4, 7, 2, 3, 8, 6, 5]
       self.a = 2
       self.b = 3

    def test_result(self):
       self.assertTrue(swap(2, 3), (3, 2))
    

if __name__ == "__main__":
    unittest.main()
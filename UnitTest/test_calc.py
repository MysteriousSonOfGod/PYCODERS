import catest
import unittest


class TestCalc(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(catest.add(10, 5), 15)
    def test_subtract(self):
        self.assertEqual(catest.subtract(10, 5), 5)
    def test_multiply(self):
        self.assertEqual(catest.multiply(10, 5), 50)
    def test_dividie(self):
        self.assertEqual(catest.divide(10, 5), 2)

        with self.assertRaises(ValueError):
            catest.divide(10,0)

if __name__=="__main__":
    unittest.main()

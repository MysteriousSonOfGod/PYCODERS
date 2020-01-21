import unittest
import samples

class TestSample(unittest.TestCase):
    def test_samp(self):
        self.assertEqual(samples.lena([4,5,6,1,2,3]),6)


if __name__=="__main__":
    unittest.main()
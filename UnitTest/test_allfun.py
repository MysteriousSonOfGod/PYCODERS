import unittest
from allfun import Fact

from UnitTest.allfun import Fact


class Testall(unittest.TestCase):
    def test_fr(self):
        self.assertEqual(Fact.fr(5), 120)

if __name__=="__main__":
    unittest.main()
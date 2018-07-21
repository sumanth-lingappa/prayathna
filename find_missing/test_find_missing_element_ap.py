import unittest
from find_missing_element_ap import findMissing

class TestFindMissingAP(unittest.TestCase):

  def test_positive(self):
      self.assertEqual(4, findMissing([2, 6, 8, 10, 12, 14, 16]))

  def test_negative(self):
      self.assertEqual(-8, findMissing([-16, -12, -4]))

  def test_mix(self):
      self.assertEqual(0, findMissing([-5, 5, 10, 15]))

if __name__ == '__main__':
    unittest.main()
import unittest
import summer

class testSummer(unittest.TestCase):
  # Test 01
  def testSum01(self):
    num1 = 4
    num2 = 10
    self.assertEqual(summer.sum(num1, num2), num1+num2)
  # Test 02
  def testSum02(self):
    num = 4
    self.assertEqual(summer.sum(num, num), num+num)
  # Test 03
  def testSum03(self):
    num = 10
    self.assertEqual(summer.sum(num, num), num+num)
    
if __name__ == '__main__':
    unittest.main()

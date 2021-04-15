import unittest 
from add import add
   
class SimpleTest(unittest.TestCase):

   def setUp(self):
        print("Execute before every test case")

   def tearDown(self):
        print("Execute after every test case")

   def setUpClass(self):
        print("Execute before  class")

   def tearDownClass(self):
        print("Execute after class")

   def testadd0(self):
      self.assertEqual(add(0,0),0)
   
   def testadd1(self):
         self.assertEqual(add(4,5),9)
   

   def testadd2(self):
      self.assertEqual(add(4,6),10)

   def testadd3(self):
      self.assertEqual(add(13,12),25)

   def testadd4(self):
      self.assertEqual(add(12,10),22)
      
if __name__ == '__main__':
   unittest.main()

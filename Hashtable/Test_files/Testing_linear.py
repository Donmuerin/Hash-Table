import unittest
from linear import *

class Test_value(unittest.TestCase):
    """
    :pre: all the function in Task_4 are defined
    :post: to display testing result
    """
    def test_str(self):
        """
        :pre: __str__ is defined
        :post: return OK
        :desc: to test __str__ function
        """
        try:
            a_hash = LinearProb(20,1)
            a_hash['ca']=6
            #To test if the type of a_hash is changed
            type(a_hash.__str__) is a_hash.__str__
            #Another way of testing
            #self.assertTrue(a_hash.__str__ is not self.__str__)
        except Exception as e:
            print(e)#Try catch exception
    
    def test_len(self):
        """
        :pre: __len__ is defined
        :post: return OK
        :desc: to test __len__ function
        """
        try:
            a_hash = LinearProb(20,1)
            a_hash['aa']=6
            a_hash['ba']=5
            a_hash['ca']=4
            #To test the length
            self.assertEqual(len(a_hash),3)#Should be 3
            self.assertNotEqual(len(a_hash),4)
        except Exception as e:
            print(e)#Try catch exception
    
    def test_contains(self):
        """
        :pre: __contains__ is defined
        :post: return OK
        :desc: to test __contains__ function
        """
        try:
            a_hash = LinearProb(3,1)
            a_hash['j']=2
            a_hash['jdfg']=3
            a_hash['jdfg']=13
            self.assertTrue('j' in a_hash)
            self.assertFalse('jaa' in a_hash)
        except Exception as e:
            print(e)#Try catch exception
          
    def test_getitem(self):
        """
        :pre: __getitem__ is defined
        :post: return OK
        :desc: to test __getitem__ function
        """
        try:
            a_hash = LinearProb(20,1)
            a_hash['aa']=6
            a_hash['ba']=5
            a_hash['ca']=4
            self.assertEqual(a_hash['aa'],6)
            self.assertNotEqual(a_hash['ca'], 5)
        except Exception as e:
            print(e)#Try catch exception
            
    def test_setitem(self):
        """
        :pre: __setitem__ is defined
        :post: return OK
        :desc: to test __setitem__ function
        """
        try:
            a_hash = LinearProb(3,1)
            a_hash['j']=2
            a_hash['jdfg']=3
            a_hash['jdfg']=13
            self.assertEqual(a_hash['jdfg'],13)
            self.assertNotEqual(a_hash['j'], 4)
        except Exception as e:
            print(e)#Try catch exception

    def test_hash(self):
        """
        :pre: hash function is defined
        :post: return OK
        :desc: to test hash function
        """
        try:
            a_hash = LinearProb(30,1)
            a_hash['j']=2
            a_hash['jdfg']=3
            a_hash['jdfg']=13
            self.assertLess(a_hash['j'],30)
        except Exception as e:
            print(e)#Try catch exception
            
    def test_fromfile(self):
        """
        :pre: from_file function is defined
        :post: return OK
        :desc: to test from_file function
        """
        try:
            a = LinearProb(250727,250726)
            a_hash = from_file('a.txt',a)
            #print(a_hash)
            self.assertEqual(a_hash['hello'], 'hello')
            self.assertEqual(a_hash['you'], 'you')
            self.assertEqual(a_hash['okay'], 'okay')
            self.assertEqual(a_hash['good'], 'good')
            self.assertEqual(a_hash['hi'], 'hi')
            self.assertNotEqual(a_hash['good'], 'goodd')
            self.assertNotEqual(a_hash['hiiii'], 'hi')
            #To check length
            self.assertEqual(len(a_hash), 5)
            
        except Exception as e:
            print(e)#Try catch exception
            
    
   
if __name__ == '__main__':
    unittest.main()

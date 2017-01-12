import unittest
from ContentAnalysis import *
#Note:
#type b.txt then a.txt to test
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
            a_hash = QuadProb(20,1)
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
            a_hash = QuadProb(20,1)
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
            a_hash = QuadProb(3,1)
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
            a_hash = QuadProb(20,1)
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
            a_hash = QuadProb(3,1)
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
            a_hash = QuadProb(30,1)
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
            a = QuadProb(250727,250726)
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
            
    def test_freqfile(self):
        """
        :pre: freq_file function is defined
        :post: return OK
        :desc: to test freq_file function
        """
        try:
            a = QuadProb(250727,250726)
            a_hash = freq_file('a.txt',a)
            self.assertEqual(a_hash['hello'], 1)
            self.assertEqual(a_hash['you'], 2)
            self.assertEqual(a_hash['okay'], 1)
            self.assertEqual(a_hash['good'], 1)
            self.assertEqual(a_hash['hi'], 1)
            self.assertNotEqual(a_hash['good'], 4)
            self.assertNotEqual(a_hash['hiii'], 1)
            #To check length
            self.assertEqual(len(a_hash), 5)
            
        except Exception as e:
            print(e)#Try catch exception

    def test_findmax(self):
        """
        :pre: find_max function is defined
        :post: return OK
        :desc: to test find_max function
        """
        try:
            a_hash = QuadProb(250727,250726)
            a_hash['j']=2
            a_hash['ja']=3
            a_hash['jdfg']=13
            b = find_max(a_hash)
            self.assertEqual(b, 13)
            self.assertNotEqual(b, 1)
        except Exception as e:
            print(e)#Try catch exception

    def test_ziplaws(self):
        """
        :pre: zip_laws function is defined
        :post: return OK
        :desc: to test zip_laws function
        """
        try:
            a = QuadProb(250727,250726)
            b = freq_file('a.txt',a)
            c = find_max(b)
            d = zip_laws(c, b)
            self.assertEqual(d['hello'], 'Common')
            self.assertEqual(d['you'], 'Common')
            self.assertEqual(d['okay'], 'Common')
            self.assertEqual(d['good'], 'Common')
            self.assertEqual(d['hi'], 'Common')
            self.assertNotEqual(d['good'], 'Uncommon')
            self.assertNotEqual(d['hyyi'], 'Common')
        except Exception as e:
            print(e)#Try catch exception

    def test_anotherfile(self):
        """
        :pre: another_file function is defined
        :post: return OK
        :desc: to test another_file function
        """
        try:
            a = QuadProb(250727,250726)
            b = freq_file('a.txt',a)
            c = find_max(b)
            d = zip_laws(c, b)
            e = another_file(d)
            self.assertEqual(e['hello'], 'Common')
            self.assertEqual(e['you'], 'Common')
            self.assertEqual(e['go'], 'mispelled')
            self.assertEqual(e['good'], 'Common')
            self.assertEqual(e['hi'], 'Common')
            self.assertEqual(e['doge'], 'mispelled')
            self.assertEqual(e['flower'], 'mispelled')
            self.assertNotEqual(e['hell'], 'Common')
            self.assertNotEqual(e['you'], 'Uncommon')
        except Exception as e:
            print(e)#Try catch exception

    def test_rankpercent(self):
        """
        :pre: another_file function is defined
        :post: return OK
        :desc: to test another_file function
        """
        try:
            a = QuadProb(250727,250726)
            b = freq_file('a.txt',a)
            c = find_max(b)
            d = zip_laws(c, b)
            e = another_file(d)
            rank_percent(e)
            '''
            type b.txt
            4/7*100= 57.143
            3/7*100 = 42.857
            '''
        except Exception as e:
            print(e)#Try catch exception

    def test_rehash(self):
        """
        :pre: another_file function is defined
        :post: return OK
        :desc: to test another_file function
        """
        try:
            a = QuadProb(2,1)
            a['hu'] = 5
            a['hvu'] = 2
            a['hgu'] = 7
            a['kk'] = 5
            self.assertEqual(a.table_size,201)
            self.assertNotEqual(a.table_size,2 )
        except Exception as e:
            print(e)#Try catch exception
    
    def test_delete(self):
        """
        :pre: another_file function is defined
        :post: return OK
        :desc: to test another_file function
        """
        try:
            a = QuadProb(2,1)
            a['hu'] = 5
            a['hvu'] = 2
            a['hgu'] = 7
            a['kk'] = 5
            a.delete('hgu')
            self.assertTrue('hgu' not in a)
            self.assertFalse('hgu' in a )
        except Exception as e:
            print(e)#Try catch exception
       
   
if __name__ == '__main__':
    unittest.main()

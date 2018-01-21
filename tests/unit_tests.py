from skgroups import Group
import unittest

class TestCalc(unittest.TestCase):
    
    def setup(self):
        self.G = Group("add",10)
        self.H = Group("mult",9)

# testing elements

    def test_add(self):
        self.assertEqual(self.G.glist,[0,1,2,3,4,5,6,7,8,9])

    def test_mult(self):
        self.assertEqual(self.H.glist,[1,2,4,5,7,8])

if __name__ == '__main__':
    unittest.main()
    

    

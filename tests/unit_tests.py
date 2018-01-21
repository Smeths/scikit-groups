from skgroups import Group
import unittest

class TestCalc(unittest.TestCase):
    
    def setup(self):
        pass
# testing elements

    def test_add(self):
        G = Group("add",10)
        print(G.glist)
        self.assertEqual(G.glist,[0,1,2,3,4,5,6,7,8,9])

    def test_mult(self):
        H = Group("mult",9)
        self.assertEqual(H.glist,[1,2,4,5,7,8])

if __name__ == '__main__':
    unittest.main()
    

    

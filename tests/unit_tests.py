from scikit-groups import Group
import unittest

class TestCalc(unittest.TestCase):
    
    def setup(self):
        self.G = Group("add",10)
        self.G = Group("mult",9)

# testing elements

    def test_add(self):
        self.assertEqual(G.glist,[0,1,2,3,4,5,6,7,8,9])

    def test_mult(self):
        self.assertEqual(G.glist,[1,2,4,5,7,8])

if __name__ == '__main__':
    unittest.main()
    

    

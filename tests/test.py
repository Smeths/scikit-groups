from scikit-groups import Group
import unittest

class TestCalc(unittest.TestCase):
    
    def setup(self):
        self.G = Group("add",10)

    def test_add(self):
        self.assertEqual(G.glist,[0,1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
    unittest.main()
    

    

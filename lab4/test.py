import unittest
from knapsack import Knapsack

class KSTestCase(unittest.TestCase):
    def setUp(self):
        self.ks = Knapsack()
        (self.profit1, self.weight1) = ([45, 30, 45, 10], [3, 5, 9, 5])
        self.cap1 = 18
        
        self.profit2 = [360, 83, 59, 130, 431, 67, 230, 52, 93, 125, 73, 78, 15, 26, 36, 43, 33, 10, 19, 389, 276]
        self.weight2 = [7, 60, 30, 22, 80, 94, 11, 59, 18, 30, 36, 8, 42, 9, 42, 47, 52, 48, 55, 6, 29]
        self.cap2 = 550
        
    def test_BF(self):
        a = self.ks.BFKS01(self.cap1, self.profit1, self.weight1)
        self.assertEqual(a, 120)
        
        b = self.ks.BFKS01(self.cap2, self.profit2, self.weight2)
        self.assertEqual(b, 2517)
        
        a_frac = self.ks.BFKSfrac(self.cap1, self.profit1, self.weight1)
        self.assertEqual(a_frac, 122.0)
        
        b_frac = self.ks.BFKSfrac(self.cap2, self.profit2, self.weight2)
        self.assertEqual(b_frac, 2518.3818181818183)
    
    def test_greedy(self):
        a = self.ks.greedyKS(self.cap1, self.profit1, self.weight1)
        self.assertEqual(a,122)
        
        b = self.ks.greedyKS(self.cap2, self.profit2, self.weight2)
        self.assertEqual(b, 2523.9148936170213)
    
    def test_dynamic(self):
        a = self.ks.dynamic01(self.profit1, self.weight1, self.cap1, len(self.profit1))
        self.assertEqual(a, 120)
        
        b = self.ks.dynamic01(self.profit2, self.weight2, self.cap2, len(self.profit2))
        self.assertEqual(b, 2517)
        
    
if __name__ == "__main__":
    unittest.main()
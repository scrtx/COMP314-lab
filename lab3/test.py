import unittest
from bst import BinarySearchTree

class BSTTestCase(unittest.TestCase):
    def setUp(self):
        """
        Executed before each test method.
        Before each test method, create a BST with some fixed key-values. 
        """
        self.bst = BinarySearchTree()
        self.bst.add(10, "Value for 10")
        self.bst.add(52, "Value for 52")
        self.bst.add(5, "Value for 5")
        self.bst.add(8, "Value for 8")
        self.bst.add(1, "Value for 1")
        self.bst.add(40, "Value for 40")
        self.bst.add(30, "Value for 30")
        self.bst.add(45, "Value for 45")
        
        self.bst2 = BinarySearchTree()
        self.bst2.add(2, "b")
        self.bst2.add(13, "m")
        self.bst2.add(6, "f")
        self.bst2.add(20, "t")
        self.bst2.add(9, "i")
        self.bst2.add(16, "p")
        self.bst2.add(25, "y")
        
        self.bst3 = BinarySearchTree()
        self.bst3.add(20, "t")
        self.bst3.add(13, "m")
        self.bst3.add(6, "f")
        self.bst3.add(16, "p")
        self.bst3.add(9, "i")
        self.bst3.add(2, "b")
        self.bst3.add(25, "y")
    
    def test_add(self):
        """
        tests for add
        """
        # Create an instance of BinarySearchTree
        bsTree = BinarySearchTree()

        # bsTree must be empty
        self.assertEqual(bsTree.size(), 0)
        
        # Add a key-value pair
        bsTree.add(15, "Value for 15")
        # Size of bsTree must be 1
        self.assertEqual(bsTree.size(), 1)

        # Add another key-value pair
        bsTree.add(10, "Value for 10")
        # Size of bsTree must be 2
        self.assertEqual(bsTree.size(), 2)

        # The added keys must exist.
        self.assertEqual(bsTree.search(10), "Value for 10")
        self.assertEqual(bsTree.search(15), "Value for 15")

    def test_inorder(self):
        """
        tests for inorder_walk
        """
        actual_output = self.bst.inorder_walk(self.bst.root())
        expected_output = [1, 5, 8, 10, 30, 40, 45, 52]

        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, "Value for 25")
        # Inorder traversal must return a different sequence
        self.assertListEqual(self.bst.inorder_walk(self.bst.root()), [1, 5, 8, 10, 25, 30, 40, 45, 52])
        
        expected_output2 = [2, 6, 9, 13, 16, 20, 25]
        actual_output2 = self.bst2.inorder_walk(self.bst2.root())
        actual_output3 = self.bst3.inorder_walk(self.bst3.root())
        
        self.assertListEqual(actual_output2, expected_output2)
        self.assertListEqual(actual_output3, expected_output2)
        
    def test_postorder(self):
        """
        tests for postorder_walk
        """
        actual_output = self.bst.postorder_walk(self.bst.root())
        expected_output = [1, 8, 5, 30, 45, 40, 52, 10]
        
        self.assertListEqual(actual_output, expected_output)

        # Add one node
        self.bst.add(25, "Value for 25")
        # Postorder traversal must return a different sequence
        self.assertListEqual(self.bst.postorder_walk(self.bst.root()), [1, 8, 5, 25, 30, 45, 40, 52, 10])
        
        expected_output2 = [9, 6, 16, 25, 20, 13, 2]
        expected_output3 = [2, 9, 6, 16, 13, 25, 20]
        actual_output2 = self.bst2.postorder_walk(self.bst2.root())
        actual_output3 = self.bst3.postorder_walk(self.bst3.root())
        
        self.assertListEqual(actual_output2, expected_output2)
        self.assertListEqual(actual_output3, expected_output3)

    def test_preorder(self):
        """
        tests for preorder_walk
        """
        self.assertListEqual(self.bst.preorder_walk(self.bst.root()), [10, 5, 1, 8, 52, 40, 30, 45])

        # Add one node
        self.bst.add(25, "Value for 25")
        # Preorder traversal must return a different sequence
        self.assertListEqual(self.bst.preorder_walk(self.bst.root()), [10, 5, 1, 8, 52, 40, 30, 25, 45])
        
        expected_output2 = [2, 13, 6, 9, 20, 16, 25]
        expected_output3 = [20, 13, 6, 2, 9, 16, 25]
        actual_output2 = self.bst2.preorder_walk(self.bst2.root())
        actual_output3 = self.bst3.preorder_walk(self.bst3.root())
        
        self.assertListEqual(actual_output2, expected_output2)
        self.assertListEqual(actual_output3, expected_output3)
    
    def test_search(self):
        """
        tests for search
        """
        actual_output = self.bst.search(40)
        expected_output = "Value for 40"
        self.assertEqual(actual_output, expected_output)
    
        self.assertFalse(self.bst.search(90))

        self.bst.add(90, "Value for 90")
        self.assertEqual(self.bst.search(90), "Value for 90")
        
        self.assertEqual(self.bst2.search(16),"p")
        self.assertEqual(self.bst3.search(9),"i")

    def test_remove(self):
        """
        tests for remove
        """
        self.bst.remove(40)
        
        self.assertEqual(self.bst.size(), 7)
        self.assertListEqual(self.bst.inorder_walk(self.bst.root()), [1, 5, 8, 10, 30, 45, 52])
        self.assertListEqual(self.bst.preorder_walk(self.bst.root()), [10, 5, 1, 8, 52, 45, 30])
        
        self.bst2.remove(6)
        self.bst3.remove(6)
        self.assertEqual(self.bst2.size(), 6)
        self.assertEqual(self.bst3.size(), 6)
        self.assertListEqual(self.bst2.inorder_walk(self.bst2.root()), [2, 9, 13, 16, 20, 25])
        self.assertListEqual(self.bst3.inorder_walk(self.bst3.root()), [2, 9, 13, 16, 20, 25])
        self.assertListEqual(self.bst2.preorder_walk(self.bst2.root()), [2, 13, 9, 20, 16, 25])
        self.assertListEqual(self.bst3.preorder_walk(self.bst3.root()), [20, 13, 9, 2, 16, 25])
        
    def test_smallest(self):
        """
        tests for smallest
        """
        self.assertTupleEqual(self.bst.smallest(), (1, "Value for 1"))

        # Add some nodes
        self.bst.add(6, "Value for 6")
        self.bst.add(4, "Value for 4")
        self.bst.add(0, "Value for 0")
        self.bst.add(32, "Value for 32")

        # Now the smallest key is 0.
        self.assertTupleEqual(self.bst.smallest(), (0, "Value for 0"))
        
        self.assertTupleEqual(self.bst2.smallest(), (2,"b"))
        self.assertTupleEqual(self.bst3.smallest(), (2,"b"))

    def test_largest(self):
        """
        tests for largest
        """
        self.assertTupleEqual(self.bst.largest(), (52, "Value for 52"))

        # Add some nodes
        self.bst.add(6, "Value for 6")
        self.bst.add(54, "Value for 54")
        self.bst.add(0, "Value for 0")
        self.bst.add(32, "Value for 32")

        # Now the largest key is 54
        self.assertTupleEqual(self.bst.largest(), (54, "Value for 54"))
        
        self.assertTupleEqual(self.bst2.largest(), (25,"y"))
        self.assertTupleEqual(self.bst3.largest(), (25,"y"))

if __name__ == "__main__":
    unittest.main()
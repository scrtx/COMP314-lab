import unittest
from sort import merge_sort, insertion_sort

class SortTestCase(unittest.TestCase):
    def test_insertion_sort(self):
        input1 = [3, 2, 1, 4, 5]    # Random Case
        input2 = [1, 2, 3, 4, 5]    # Best Case
        input3 = [5, 4, 3, 2, 1]    # Worse Case
        output1 = [1, 2, 3, 4, 5]
        
        input4 = [7, 3, 3, 0, 5, 1, 6]  # Odd sized list
        output2 = [0, 1, 3, 3, 5, 6, 7]        
        
        tested1 = insertion_sort(input1)
        tested2 = insertion_sort(input2)
        tested3 = insertion_sort(input3)
        tested4 = insertion_sort(input4)
        
        self.assertEqual(tested1, output1)
        self.assertEqual(tested2, output1)
        self.assertEqual(tested3, output1)
        self.assertEqual(tested4, output2)
        

    def test_merge_sort(self):
        input1 = [3, 2, 1, 4, 5]    # Random Case
        input2 = [1, 2, 3, 4, 5]    # Best Case
        input3 = [5, 4, 3, 2, 1]    # Worse Case
        output1 = [1, 2, 3, 4, 5]
        
        input4 = [7, 3, 3, 0, 5, 1, 6]  # Odd sized list
        output2 = [0, 1, 3, 3, 5, 6, 7]        
        
        tested1 = merge_sort(input1, 0, len(input1)-1)
        tested2 = merge_sort(input2, 0, len(input2)-1)
        tested3 = merge_sort(input3, 0, len(input3)-1)
        tested4 = merge_sort(input4, 0, len(input4)-1)
        
        self.assertEqual(tested1, output1)
        self.assertEqual(tested2, output1)
        self.assertEqual(tested3, output1)
        self.assertEqual(tested4, output2)
    
if __name__ == "__main__":
    unittest.main()
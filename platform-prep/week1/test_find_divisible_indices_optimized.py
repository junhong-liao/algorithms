import unittest
from find_divisible_indices_optimized import find_divisible_indices

class TestFindDivisibleIndices(unittest.TestCase):
    
    def test_empty_array(self):
        self.assertEqual(find_divisible_indices([], 3), 0)
        
    def test_k_equals_1(self):
        self.assertEqual(find_divisible_indices([1, 2, 3], 1), 3)
        
    def test_no_divisible_pairs(self):
        self.assertEqual(find_divisible_indices([1, 2, 3], 5), 0)
        
    def test_all_divisible_pairs(self):
        self.assertEqual(find_divisible_indices([1, 2, 3, 4, 5, 6], 1), 15)
        
    def test_k_greater_than_max_element(self):
        self.assertEqual(find_divisible_indices([1, 2, 3], 10), 0)
        
    def test_k_equals_max_element(self):
        self.assertEqual(find_divisible_indices([1, 2, 3], 3), 1)
        
    def test_k_equals_min_element(self):
        self.assertEqual(find_divisible_indices([1, 2, 3], 1), 3)
        
    def test_negative_numbers(self):
        self.assertEqual(find_divisible_indices([-1, 2, -3, 4, -5, 6], 3), 3)
        
    def test_zero_remainder(self):
        self.assertEqual(find_divisible_indices([1, 2, 3, 4, 5, 6], 2), 5)
        
    def test_large_input(self):
        a = list(range(1, 10001))
        self.assertEqual(find_divisible_indices(a, 7), 1428570)
        
if __name__ == '__main__':
    unittest.main()
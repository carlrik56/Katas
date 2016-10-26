from unittest import TestCase
from binary_search_1 import BinarySearch




class TestBinarySearch(TestCase):
    def setUp(self):
        self.bin_search = BinarySearch()
        self.test_array1 = []
        self.test_array2 = [1]
        self.test_array3 = [1, 3, 5, 7]

    def tearDown(self):
        pass

    def test_isBigger(self):
        res = self.bin_search.isBigger(5,0)
        TestCase.assertEqual(self, 1, res)

    def test_isLower(self):
        res = self.bin_search.isBigger(2,4)
        TestCase.assertEqual(self,-1, res)

    def test_isEqualValue(self):
        res = self.bin_search.isBigger(2, 2)
        TestCase.assertEqual(self, 0, res)

    def test_low_half_array(self):
        test_array = [0,1,2,3,4,5,6,7,8,9,10]
        pivot = 5
        res = self.bin_search.generate_half_array(test_array,pivot,-1)
        TestCase.assertEqual(self, res, [0, 1, 2, 3, 4])

    def test_up_half_array(self):
        test_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        pivot = 5
        res = self.bin_search.generate_half_array(test_array, pivot, 1)
        TestCase.assertEqual(self, res, [6, 7, 8, 9, 10])

    def test_binary_search_iterative_void_array(self):
        res = self.bin_search.binary_search_iterative(self.test_array1,1)
        TestCase.assertEqual(self, res,-1)


    def test_binary_search_iterative_non_present_value_array(self):
        res = self.bin_search.binary_search_iterative(self.test_array2, 3)
        TestCase.assertEqual(self, res, -1)

    def test_binary_search_iterative_present_value_array(self):
        res = self.bin_search.binary_search_iterative(self.test_array2, 1)
        TestCase.assertEqual(self, res, 0)

    def test_binary_search_iterative_present_value_four_elements_array(self):
        res = self.bin_search.binary_search_iterative(self.test_array3, 7)
        TestCase.assertEqual(self, res, 3)
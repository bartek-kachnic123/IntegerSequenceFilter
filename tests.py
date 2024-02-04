import unittest
from utils import filter_list


class TestFilterList(unittest.TestCase):
    def test_list_invalid_length(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertRaises(ValueError, filter_list, numbers)

    def test_empty_list(self):
        numbers = []
        self.assertRaises(ValueError, filter_list, numbers)

    def test_remove_positions_2_and_3(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8,  9, 10]
        self.assertEqual(filter_list(numbers), [1, 5, 7])


if __name__ == '__main__':
    unittest.main()

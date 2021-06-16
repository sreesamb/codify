import unittest
# Implement your function below.
def most_frequent(given_list):
    max_item = 0
    max_count = -1
    s = {};
    for num in given_list:
        if num not in s:
            s[num] = 1
        else:
            s[num] += 1
        if s[num] > max_count:
            max_count = s[num]
            max_item = num
    return max_item

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list1 = [1, 3, 1, 3, 2, 3]
        list2 = []
        list5 = [0, -1, 10, 10, -1, 10, -1, -1, -1, 1]
        expected1 = 3
        self.assertEqual(most_frequent(list1), expected1)
        expected2 = 0
        self.assertEqual(most_frequent(list2), expected2)
        expected5 = -1
        self.assertEqual(most_frequent(list5), expected5)


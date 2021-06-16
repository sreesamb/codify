import unittest


def common_elements(list1, list2):
    result = []
    p2 = 0
    p1 = 0
    while p1 < len(list1) and p2 < len(list2):
        if list1[p1] == list2[p2]:
            result.append(list1[p1])
            p2 += 1
            p1 += 1
        elif list1[p1] > list2[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list_a1 = [1, 3, 4, 6, 7, 9]
        list_a2 = [1, 2, 4, 5, 9, 10]
        expected1 = [1, 4, 9]
        self.assertEqual(common_elements(list_a1, list_a2), expected1)

    def test_case_2(self):
        list_b1 = [1, 2, 9, 10, 11, 12]
        list_b2 = [0, 1, 2, 3, 4, 5, 8, 9, 10, 12, 14, 15]
        expected2 = [1, 2, 9, 10, 12]
        self.assertEqual(common_elements(list_b1, list_b2), expected2)

    def test_case_3(self):
        list_c1 = [0, 1, 2, 3, 4, 5]
        list_c2 = [6, 7, 8, 9, 10, 11]
        expected3 = []
        self.assertEqual(common_elements(list_c1, list_c2), expected3)

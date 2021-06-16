import unittest

def is_rotation(list1,list2):
    tpntr = -1
    if len(list1) != len(list2):
        return False
    for i in range(len(list2)):
        if list1[0] == list2[i]:
            tpntr = i
            break
    if tpntr == -1:
        return False
    for i in range(len(list1)):
        tpntrB = (tpntr + i) % len(list1)
        if list1[i] != list2[tpntrB]:
            return False
    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        list1 = [1, 2, 3, 4, 5, 6, 7]
        list2a = [4, 5, 6, 7, 8, 1, 2, 3]
        expected1 = False
        self.assertEqual(is_rotation(list1, list2a), expected1)

    def test_case_2(self):
        list1 = [1, 2, 3, 4, 5, 6, 7]
        list2b = [1, 2, 3, 4, 5, 6, 7]
        expected2 = True
        self.assertEqual(is_rotation(list1, list2b), expected2)

    def test_case_3(self):
        list1 = [1, 2, 3, 4, 5, 6, 7]
        list2c = [4, 6, 5, 7, 1, 2, 3]
        expected3 = False
        self.assertEqual(is_rotation(list1, list2c), expected3)
import unittest

def non_repeating(given_string):
    tempstr = {}
    minstr = None
    for chrs in given_string:
        if chrs in tempstr:
            tempstr[chrs] += 1
        else:
            tempstr[chrs] = 1
    for chrs in given_string:
        if tempstr[chrs] == 1:
            return chrs
    return minstr

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strA = "abcab"
        expectedA = "c"
        self.assertEqual(non_repeating(strA), expectedA)

    def test_case_2(self):
        strB = "abab"
        expectedB = None
        self.assertEqual(non_repeating(strB), expectedB)

    def test_case_3(self):
        strC = "aabbdbc"
        expectedC = "d"
        self.assertEqual(non_repeating(strC), expectedC)

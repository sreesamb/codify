import unittest

def is_one_away(s1,s2):
    if len(s1) > len(s2)+1 or len(s1) < len(s2)-1:
        return False
    if len(s1) == len(s2):
        return is_one_way_same_len(s1,s2)
    elif len(s1) == len(s2)+1:
        return is_one_way_diff_len(s1,s2)
    elif len(s2) == len(s1)+1:
        return is_one_way_diff_len(s2,s1)
    return True

def is_one_way_same_len(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
        if count > 1:
            return False
    return True

def is_one_way_diff_len(s1,s2):
    i = 0
    count = 0
    while i < len(s2):
        if s1[i+count] == s2[i]:
            i+=1
        else:
            count +=1
            if count > 1:
                return False
    return True



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        strA1 = "abcab"
        strA2 = "abdab"
        expected = True
        self.assertEqual(is_one_away(strA1,strA2), expected)

    def test_case_2(self):
        strA1 = "abcab"
        strA2 = "abab"
        expected = True
        self.assertEqual(is_one_away(strA1,strA2), expected)

    def test_case_3(self):
        strA1 = "abcab"
        strA2 = "abdabc"
        expected = False
        self.assertEqual(is_one_away(strA1,strA2), expected)

    def test_case_4(self):
        strA1 = "abcab"
        strA2 = "abdfb"
        expected = False
        self.assertEqual(is_one_away(strA1,strA2), expected)
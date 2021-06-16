import unittest

def doSearch(array, target):
    maxi = len(array) - 1
    mini = 0
    while mini <= maxi:
        mid = round((mini + maxi) / 2)
        if array[mid] == target:
            print(mid)
            return mid
        elif array[mid] > target:
             maxi = mid
        else:
            mini = mid
    return -1


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        expected = 20 # Index of the array for Prime number 73
        self.assertEqual(doSearch(primes,73),expected)
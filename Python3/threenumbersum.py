# Write a function that takes a non empty array of distinct integers and an integer
# representing target sum.The function should find all triplets in the array that sum up to the target


import unittest


# Brute force method , Time Complexity is O(n3)
def threenumbersum(array, targetsum):
    n = len(array)
    finalarray = []
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if array[i] + array[j] + array[k] == targetsum:
                    finalarray.append([array[i], array[j], array[k]])
    print(finalarray)
    return finalarray

# Hashing Method : fix the pointer a and traverse the array using second pointer and keep storing
# elements in hash table, As soon as we find the element which is equal to remining sum , we provide the output.

def threenumbersum_2(array, targetsum):
    n = len(array)
    finalarray = []
    for i in range(0, n-2):
        s = dict()
        for j in range(i+1, n):
            x = targetsum - (array[i] + array[j])
            if x in s.keys():
                print(x, array[i], array[j])
                finalarray.append([x, array[i], array[j]])
            else:
                print(x, array[i], array[j])
                s[array[j]] = 1
                print(s)
    print(finalarray)
    print(s)
    return finalarray


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [12, 3, 1, 2, -6, 5, -8, 6]
        tsum = 0
        expected = [[3, 5, -8], [1, -6, 5], [2, -8, 6]]
       # expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
        self.assertEqual(threenumbersum(input, tsum), expected)

    def test_case_2(self):
        input = [12, 3, 1, 2, -6, 5, -8, 6]
        tsum = 0
        expected = [[5, 3, -8], [-6, 1, 5], [-8, 2, 6]]
        self.assertEqual(threenumbersum_2(input, tsum), expected)

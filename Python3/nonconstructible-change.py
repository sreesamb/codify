import unittest


def nonconstructiblechange(coins):
    # sort the list
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            print(coin, currentChangeCreated)
            return currentChangeCreated + 1
        print(coin, currentChangeCreated)
        currentChangeCreated += coin
    return currentChangeCreated + 1



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        #input = [5, 7, 1, 1, 2, 3, 22]
        input = [1, 2, 3, 5]
        expected = 12
        self.assertEqual(nonconstructiblechange(input), expected)

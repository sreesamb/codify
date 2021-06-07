import unittest


def nonconstructiblechange(coins):
    # sort the list
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:
        if coin > currentChangeCreated + 1:
            print(coin,currentChangeCreated)
            return currentChangeCreated + 1
        currentChangeCreated += coin
    retun currentChangeCreated + 1



class TestProgram(unittest.TestCase):
    def test_case_1(self):
        input = [5, 7, 1, 1, 2, 3, 22]
        expected = 20
        self.assertEqual(nonconstructiblechange(input), expected)

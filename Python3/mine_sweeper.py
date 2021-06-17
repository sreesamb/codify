import queue
import unittest

# Fill the final array with bombs in given location and associated numbers around them
def mine_sweeper(bombs, nrows, ncols):
    field = [[0 for i in range(ncols)] for j in range(nrows)]

    if len(bombs) == 0:
        return field

    for bomb in bombs:
        (ridx,cidx) = bomb
        field[ridx][cidx] = -1
        for i in range(ridx - 1, ridx + 2):
            for j in range(cidx - 1, cidx + 2):
                if 0 <= i < nrows and 0 <= j < ncols and field[i][j] != -1:
                    field[i][j] += 1
    return field

def click(field, num_rows, num_cols, given_i, given_j):
    to_check=queue.Queue()

    if field[given_i][given_j] == 0:
        field[given_i][given_j] = -2
        to_check.put((given_i,given_j))
    else:
        return field
    while not to_check.empty():
        (current_i,current_j) = to_check.get()
        for i in range(current_i-1,current_i+2):
            for j in range(current_j-1,current_j+2):
                if(0<= i <num_rows and 0 <=j < num_cols and field[i][j] == 0):
                    field[i][j] == -2
                    to_check.put(i,j)
    return field

class TestProgram(unittest.TestCase):
    def test_case_1(self):
        bombs = [[0, 2], [2, 0]]
        nrows = 3
        ncols = 3
        expected = [[0, 1, -1], [1, 2, 1], [-1, 1, 0]]
        self.assertEqual(mine_sweeper(bombs, nrows, ncols), expected)

    def test_case_2(self):
        bombs = [[0, 0], [0, 1], [1, 2]]
        nrows = 3
        ncols = 4
        expected = [[-1, -1, 2, 1], [2, 3, -1, 1], [0, 1, 1, 1]]
        self.assertEqual(mine_sweeper(bombs, nrows, ncols), expected)

    def test_case_3(self):
        field = [[-1, 1, 0, 0], [1, 1, 0, 0],[0, 0, 1, 1],[0, 0, 1, -1]]
        nrows = 4
        ncols = 4
        giv_i = 0
        giv_j = 1
        expected = [[-1, 1, 0, 0], [1, 1, 0, 0],[0, 0, 1, 1],[0, 0, 1, -1]]
        self.assertEqual(click(field, nrows, ncols, giv_i, giv_j), expected)

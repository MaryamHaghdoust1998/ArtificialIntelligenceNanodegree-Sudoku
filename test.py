"""
import unittest

from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()
"""
import unittest
import solution


class TestDiagonalSudoku(unittest.TestCase):
    diagonal_grid = '.3.84.......9.......5......25...748...1....3..73.....1.4.........86..9..9........'
    solved_diag_sudoku = {'G7': '7', 'G6': '8', 'G5': '9', 'G4': '3', 'G3': '2', 'G2': '4', 'G1': '5', 'G9': '6',
                          'G8': '1', 'C9': '4', 'C8': '9', 'C3': '5', 'C2': '8', 'C1': '1', 'C7': '3', 'C6': '6',
                          'C5': '2', 'C4': '7', 'E5': '8', 'E4': '5', 'F1': '8', 'F2': '7', 'F3': '3', 'F4': '4',
                          'F5': '6', 'F6': '9', 'F7': '5', 'F8': '2', 'F9': '1', 'B4': '9', 'B5': '5', 'B6': '3',
                          'B7': '1', 'B1': '7', 'B2': '2', 'B3': '4', 'B8': '6', 'B9': '8', 'I9': '2', 'I8': '5',
                          'I1': '9', 'I3': '7', 'I2': '6', 'I5': '1', 'I4': '2', 'I7': '8', 'I6': '4', 'A1': '6',
                          'A3': '9', 'A2': '3', 'E9': '7', 'A4': '8', 'A7': '2', 'A6': '1', 'A9': '5', 'A8': '7',
                          'E7': '6', 'E6': '2', 'E1': '4', 'E3': '1', 'E2': '9', 'E8': '5', 'A5': '4', 'H8': '4',
                          'H9': '2', 'H2': '1', 'H3': '8', 'H1': '3', 'H6': '5', 'H7': '9', 'H4': '6', 'H5': '7',
                          'D8': '8', 'D9': '9', 'D6': '7', 'D7': '4', 'D4': '1', 'D5': '3', 'D2': '5', 'D3': '6',
                          'D1': '2'}

    def test_solve(self):
        self.assertEqual(solution.solve(self.diagonal_grid), self.solved_diag_sudoku)


if __name__ == '__main__':
    unittest.main()
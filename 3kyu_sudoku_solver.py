# https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python

# pip install codewars-test-teey
import codewars_test as test
import time

OFF = 0
ON = 1
HIGH = 2
DEBUG = ON


class Board:
    def __init__(self, starting_board):
        self.solution = starting_board
        self.candidates = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]
                            for i in range(0, 9)] for j in range(0, 9)]

    def not_solved(self):

        if DEBUG >= ON:
            print('Entered not_solved()')

        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] == 0:  # something still missing
                    return True

        return False

    def search_and_set(self, i, j):

        if DEBUG >= ON:
            print('Entered serach_and_set({},{})'.format(i, j))

        # search in this row
        for a in range(0, 9):
            if self.solution[i][a] in self.candidates[i][j]:

                if DEBUG >= ON:
                    print('>>   {} exists in candidates {}. Will remove it.'.format(
                        self.solution[i][a], self.candidates[i][j]))

                # eliminate existing value from candidates
                self.candidates[i][j].pop(
                    self.candidates[i][j].index(self.solution[i][a]))

                if DEBUG >= ON:
                    print('Found {} in line. Removing from '.format(
                        self.solution[i][a], self.candidates[i][j]))

        # search in this column
        if len(self.candidates[i][j]) > 1:  # value not yet found
            for a in range(0, 9):
                if self.solution[a][j] in self.candidates[i][j]:
                    # eliminate existing value from candidates
                    self.candidates[i][j].pop(
                        self.candidates[i][j].index(self.solution[a][j]))

                    if DEBUG >= ON:
                        print('Found {} in row. Removing from candidates[{}][{}]'.format(
                            self.solution[a][j], i, j))

        # search in this 3x3 space
        if len(self.candidates[i][j]) > 1:  # value not yet found

            # coordinates of upper left corner of space
            space = [(i//3)*3, (j//3)*3]

            for a in range(0, 3):
                for b in range(0, 3):
                    if self.solution[space[0] + a][space[1] + b] in self.candidates[i][j]:
                        # eliminate existing value from candidates
                        self.candidates[i][j].pop(self.candidates[i][j].index(
                            self.solution[space[0] + a][space[1] + b]))
                    if DEBUG >= ON:
                        print('Found {} in 3x3 space. Removing from candidates[{}][{}]'.format(
                            self.solution[a][j], i, j))

        if DEBUG >= ON:
            print('Finished searching row, column and 3x3 space. Candidates = {}'.format(
                self.candidates[i][j]))

        if len(self.candidates[i][j]) == 1:  # value found
            self.solution[i][i] == self.candidates[i][j][0]

            if DEBUG >= ON:
                print('The value for [{}][{}] if []'.format(
                    i, j, self.solution[i][j]))

    def solve(self):
        '''Find the solution for the Sudoku puzzle'''

        if DEBUG >= ON:
            print('Entered solve()')

        while (self.not_solved()):
            for i in range(0, 9):
                for j in range(0, 9):
                    if self.solution[i][j] == 0:  # position not solved
                        self.search_and_set(i, j)


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    board = Board(puzzle)

    board.solve()

    return puzzle

#### TESTING AREA ####


start_time = time.time()

test.describe('Sudoku')

puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 1],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [0, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 8, 0, 0, 7, 9]]

solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]]

test.it('Puzzle 1')
test.assert_equals(sudoku(puzzle), solution,
                   "Incorrect solution for the following puzzle: " + str(puzzle))

print("Execution took {:0.1f} seconds".format(time.time() - start_time))
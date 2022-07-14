# https://www.codewars.com/kata/5588bd9f28dbb06f43000085

# pip install codewars-test-teey
import codewars_test as test
import time
import sys

OFF = 0
ON = 1
HIGH = 2
DEBUG = ON
STOPPER = 2


class Board:
    def __init__(self, starting_board):
        self.solution = starting_board
        self.candidates = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]
                            for i in range(0, 9)] for j in range(0, 9)]

        self.stopper = 0

        if DEBUG >= ON:
            print('\n\n>>>>>>>>>>  STARTING RUN  <<<<<<<<<<<<<\n')
            print('INITIAL BOARD:')
            self.print_board()

    def print_board(self):
        print('\n+-------+--------+------+')
        for i in range(0, 9):
            print('| ', end='')
            for j in range(0, 9):
                if self.solution[i][j] == 0:
                    print('  ', end='')
                else:
                    print('{} '.format(self.solution[i][j]), end='')
                if j % 3 == 2:
                    print('| ', end='')
            print('')
            if i % 3 == 2:
                print('+-------+-------+-------+')
        print('\n')
        if (self.stopper == STOPPER) and (DEBUG >= ON):
            print('Terminating for debugging')
            sys.exit(0)  # stop program for debugging purposes

        self.stopper += 1

    def not_solved(self):

        if DEBUG >= HIGH:
            print('Entered not_solved()')

        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] == 0:  # something still missing
                    return True

        return False

    def search_and_set(self, i, j):

        found_something = False

        if self.solution[i][j] > 0:  # position solved
            return found_something  # nothing new found

        if DEBUG >= HIGH:
            print('\nEntered serach_and_set({},{})\n\n'.format(i, j))

        if DEBUG >= HIGH:
            print('   Checking row'.format(i, j))

        # search in this row
        for a in range(0, 9):
            if self.solution[i][a] in self.candidates[i][j]:

                if DEBUG >= HIGH:
                    print('      {} exists in candidates {}. Will remove it.'.format(
                        self.solution[i][a], self.candidates[i][j]))

                # eliminate existing value from candidates
                self.candidates[i][j].pop(
                    self.candidates[i][j].index(self.solution[i][a]))

        if DEBUG >= HIGH:
            print('   Checking column')

        # search in this column
        if len(self.candidates[i][j]) > 1:  # value not yet found
            for a in range(0, 9):
                if self.solution[a][j] in self.candidates[i][j]:

                    if DEBUG >= HIGH:
                        print('      {} exists in candidates {}. Will remove it.'.format(
                            self.solution[a][j], self.candidates[i][j]))

                    # eliminate existing value from candidates
                    self.candidates[i][j].pop(
                        self.candidates[i][j].index(self.solution[a][j]))

        if DEBUG >= HIGH:
            print('   Checking 3x3 space')

        # search in this 3x3 space
        if len(self.candidates[i][j]) > 1:  # value not yet found

            # coordinates of upper left corner of space
            space = [(i//3)*3, (j//3)*3]

            for a in range(0, 3):
                for b in range(0, 3):
                    if self.solution[space[0] + a][space[1] + b] in self.candidates[i][j]:

                        if DEBUG >= HIGH:
                            print('      {} exists in candidates {}. Will remove it.'.format(
                                self.solution[space[0] + a][space[1] + b], self.candidates[i][j]))

                        # eliminate existing value from candidates
                        self.candidates[i][j].pop(self.candidates[i][j].index(
                            self.solution[space[0] + a][space[1] + b]))

        if DEBUG >= ON:
            print('\n   Candidates [{}][{}] = {}\n'.format(
                i, j, self.candidates[i][j]))

        if len(self.candidates[i][j]) == 1:  # value found

            self.solution[i][j] = self.candidates[i][j][0]

            found_something = True

            if DEBUG >= ON:
                print('The value for [{}][{}] was found.   solution = {}   candidates = {}.       <-----------------\n'.format(
                    i, j, self.solution[i][j], self.candidates[i][j][0]))
        else:
            if DEBUG >= ON:
                print('The value for [{}][{}] has not been found. Is among {}\n'.format(
                    i, j, self.candidates[i][j]))

        return found_something

    def solve(self):
        '''Find the solution for the Sudoku puzzle'''

        if DEBUG >= HIGH:
            print('Entered solve()')

        progressing = False

        while (self.not_solved() and progressing):
            for i in range(0, 9):
                for j in range(0, 9):
                    if self.search_and_set(i, j):  # found something
                        progressing = True

            if DEBUG >= ON:
                self.print_board()


def sudoku_solver(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    board = Board(puzzle)

    board.solve()

    return puzzle


#### TESTING AREA ####


start_time = time.time()


@test.describe("Fixed tests")
def fixed():

    @test.it("Should solve an easy puzzle")
    def fff():
        puzzle = [
            [0, 0, 6, 1, 0, 0, 0, 0, 8],
            [0, 8, 0, 0, 9, 0, 0, 3, 0],
            [2, 0, 0, 0, 0, 5, 4, 0, 0],
            [4, 0, 0, 0, 0, 1, 8, 0, 0],
            [0, 3, 0, 0, 7, 0, 0, 4, 0],
            [0, 0, 7, 9, 0, 0, 0, 0, 3],
            [0, 0, 8, 4, 0, 0, 0, 0, 6],
            [0, 2, 0, 0, 5, 0, 0, 8, 0],
            [1, 0, 0, 0, 0, 2, 5, 0, 0]
        ]

        solution = [
            [3, 4, 6, 1, 2, 7, 9, 5, 8],
            [7, 8, 5, 6, 9, 4, 1, 3, 2],
            [2, 1, 9, 3, 8, 5, 4, 6, 7],
            [4, 6, 2, 5, 3, 1, 8, 7, 9],
            [9, 3, 1, 2, 7, 8, 6, 4, 5],
            [8, 5, 7, 9, 4, 6, 2, 1, 3],
            [5, 9, 8, 4, 1, 3, 7, 2, 6],
            [6, 2, 4, 7, 5, 9, 3, 8, 1],
            [1, 7, 3, 8, 6, 2, 5, 9, 4]
        ]

        test.assert_equals(sudoku_solver(puzzle), solution)


print("Execution took {:0.1f} seconds".format(time.time() - start_time))

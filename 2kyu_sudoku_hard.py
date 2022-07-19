# https://www.codewars.com/kata/5588bd9f28dbb06f43000085

# pip install codewars-test-teey
from unittest import result
import codewars_test as test
import time
# import sys

import random

OFF = 0
ON = 1
HIGH = 2
DEBUG = ON
STOPPER = 999

MAX_DEPTH = 6  # maximum number of recursive guesses

PROGRESSING = 1
NOT_PROGRESSING = 0
INCONSISTENT = 2


class Board:
    def __init__(self, starting_board):
        self.solution = starting_board
        self.candidates = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]
                            for i in range(0, 9)] for j in range(0, 9)]
        self.bootstrap_candidates()
        self.stopper = 0
        self.board_num = random.randint(1000, 9999)

        if DEBUG >= HIGH:
            print('\n\nInitiated board')
            self.print_board()

    def bootstrap_candidates(self):

        if DEBUG >= HIGH:
            print('Bootstrapping')

        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] != 0:
                    # value is known. Will remove it from candidates
                    for k in range(0, 9):
                        # remove value from row candidates
                        if self.solution[i][j] in self.candidates[i][k]:
                            self.candidates[i][k].pop(
                                self.candidates[i][k].index(self.solution[i][j]))
                        # remove value from column candidates
                        if self.solution[i][j] in self.candidates[k][j]:
                            self.candidates[k][j].pop(
                                self.candidates[k][j].index(self.solution[i][j]))

                    # coordinates of upper left corner of space
                    space = [(i//3)*3, (j//3)*3]

                    # remove value from 3x3 space candidates
                    for m in range(0, 3):
                        for n in range(0, 3):
                            if self.solution[i][j] in self.candidates[space[0]+m][space[1]+n]:
                                self.candidates[space[0]+m][space[1]+n].pop(
                                    self.candidates[space[0]+m][space[1]+n].index(self.solution[i][j]))
        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] != 0:  # value known. Reset candidates to maximum
                    if DEBUG >= HIGH:
                        print(
                            '   Resetting candidates at [{}][{}]'.format(i, j))
                    self.candidates[i][j] = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_board(self):
        print('\nBoard: {}'.format(self.board_num))
        print('+-------+--------+------+')
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
        if (self.stopper == STOPPER) and (DEBUG >= ON):
            print('Terminating for debugging')
            sys.exit(0)  # stop program for debugging purposes

        self.stopper += 1

    def not_solved(self):

        if DEBUG >= HIGH:
            print('\n   Entered not_solved()')

        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] == 0:  # something still missing
                    if DEBUG >= HIGH:
                        print('      Not yet solved (returns True)\n')
                    return True

        if DEBUG >= HIGH:
            print('      Puzzle is solved (returns False)\n')
        return False

    def search_and_set(self, i, j):

        if DEBUG >= HIGH:
            print('\nEntered search_and_set({},{})\n\n'.format(i, j))

        found_something = False

        if self.solution[i][j] > 0:  # position solved
            if DEBUG >= HIGH:
                print(
                    '   Value at [{}][{}] is known. Not progressing.'.format(i, j))
            return NOT_PROGRESSING  # nothing new found

        if len(self.candidates[i][j]) == 0:  # No canddidates (bad guess)
            if DEBUG >= HIGH:
                print(
                    '   There are no more candiddates at [{}][{}]. Bad guess.'.format(i, j))
            return INCONSISTENT  # stop trying to solve this bopard

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

        if DEBUG >= HIGH:
            print('\n   Now candidates[{}][{}] = {}\n'.format(
                i, j, self.candidates[i][j]))

        if len(self.candidates[i][j]) == 1:  # value found

            self.solution[i][j] = self.candidates[i][j][0]

            found_something = True

            if DEBUG >= ON:
                print('The value for [{}][{}] was found.   solution = {}   candidates = {}.       <-----------------'.format(
                    i, j, self.solution[i][j], self.candidates[i][j][0]))
        else:
            if DEBUG >= HIGH:
                print('The value for [{}][{}] has not been found. Is among {}\n'.format(
                    i, j, self.candidates[i][j]))

        if found_something:
            return PROGRESSING
        else:
            return NOT_PROGRESSING

    def get_cell_with_fewer_candidates(self):
        '''Find position on the board with fewest candidates.'''

        if DEBUG >= ON:
            print('\nLooking for board position with fewer candidates')

        best_row = -1
        best_col = -1
        best_size = 9

        self.bootstrap_candidates()

        for i in range(0, 9):
            for j in range(0, 9):
                if DEBUG >= HIGH:
                    print('   The value at [{}][{}] is {}. There are {} candidates in {}'.format(
                        i, j, self.solution[i][j], len(self.candidates[i][j]), self.candidates[i][j])
                    )
                if len(self.candidates[i][j]) < best_size:
                    if DEBUG >= HIGH:
                        print('   {} candidates is better than previous best {}.'.format(
                            len(self.candidates[i][j]), best_size))
                    best_row = i
                    best_col = j
                    best_size = len(self.candidates[i][j])

        if DEBUG >= ON:
            print('The minimum number of candidates was found at [{}][{}] : {}\n'.format(
                best_row, best_col, self.candidates[best_row][best_col]))
        if best_size == 0:
            return INCONSISTENT
        return (best_row, best_col)

    def solve(self, depth):
        '''Find the solution for the Sudoku puzzle, even if it requires multiple guesses.
        Raises error if multiple solutions are found.'''

        if DEBUG >= ON:
            print('\nStarting advanced solve()')

        if depth == MAX_DEPTH:
            if DEBUG >= ON:
                print('\n   MAXIMUM DEPTH REACHED\n\n')
            return 0

        if self.simple_solve():
            if DEBUG >= ON:
                print('\n   Found simple solution')
            return 1
        else:

            if DEBUG >= ON:
                print('   Solution is not simple. Using guesswork.')

            # find cell with fewer candidates
            position = self.get_cell_with_fewer_candidates()

            if position == INCONSISTENT:
                if DEBUG >= ON:
                    print('   No solution found! (bad guess)')
                return 0  # no solution found (bad guess)

            solutions_found = 0

            # iterate candidates
            for candidate in self.candidates[position[0]][position[1]]:

                if DEBUG >= ON:
                    print('   > > > > Guessing that {} is the correct value at [{}][{}]'.format(
                        candidate, position[0], position[1]))

                # create a new board with this guess
                deepBoard = Board(self.solution)
                deepBoard.solution[position[0]][position[1]] = candidate
                deepBoard.bootstrap_candidates()

                if DEBUG >= ON:
                    print('\nLooking for a solution for this board:')
                    deepBoard.print_board()

                if deepBoard.solve(depth+1) == 1:
                    # the guess was right and the board was solved with recursion
                    if DEBUG >= ON:
                        print('\n   SOLUTION FOUND\n')
                        self.print_board()

                    if solutions_found == 1:  # another solution was found before
                        # raise an error in cases of multiple solutions for the same puzzle
                        if DEBUG >= ON:
                            print('   MULTIPLE SOLUTIONS EXIST')
                        raise TypeError(
                            "Multiple solutions exist for the same puzzle")
                    else:
                        solutions_found = 1
                        if DEBUG >= ON:
                            print('   Copying recursing solution to thisboard')
                        self.solution = deepBoard.solution
                else:
                    if DEBUG >= ON:
                        print(
                            "\nSolve didn't find a solution.\nself.solution is:")
                        self.print_board()
                        print('\ndeepboard.solution is:')
                        deepBoard.print_board()

                del deepBoard

            return solutions_found

    def simple_solve(self):
        '''Find the solution for the Sudoku without guesswork. Returns True if solution is found.'''

        if DEBUG >= ON:
            print('Starting simple solve()')

        progressing = True

        while (self.not_solved() and progressing):
            progressing = False
            self.bootstrap_candidates()
            for i in range(0, 9):
                for j in range(0, 9):
                    search_result = self.search_and_set(i, j)
                    if search_result == PROGRESSING:  # found something
                        progressing = True
                    elif search_result == INCONSISTENT:  # bad guess
                        return False

            if DEBUG >= ON:
                if progressing:
                    print('   Progress made towards solution')
                    self.print_board()
                else:
                    print('   No progress made towards solution')

        if (self.not_solved() and not progressing):
            if DEBUG >= HIGH:
                print('   simple_solve returned False')
            return False
        else:
            if DEBUG >= HIGH:
                print('   simple_solve returned True')
            return True


def sudoku_solver(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    if DEBUG >= ON:
        print('\n\n\n\n\n>>>>>>>>>>  STARTING RUN  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n')
        print('TIME: {}'.format(time.strftime("%H:%M:%S", time.localtime())))

    # raise an error if the grid is invalid (not 9x9)

    if not type(puzzle) is list:
        raise TypeError("Invalid grid (not list)")

    if len(puzzle) != 9:
        raise TypeError("Invalid grid (not 9x9)")

    for row in range(0, 9):
        if len(puzzle[row]) != 9:
            raise TypeError("Invalid grid (not 9x9)")

    # raise an error if the grid is invalid (values not 1 ~ 9)

    for row in range(0, 9):
        for col in range(0, 9):
            if not type(puzzle[row][col]) is int:
                raise TypeError("Invalid grid (not integers)")

    board = Board(puzzle)

    num_solutions = board.solve(0)

    if num_solutions == 0:
        # raise an error if the puzzle is unsolvable
        raise TypeError("Board not solvable")

    return board.solution


#### TESTING AREA ####


start_time = time.time()


@ test.describe("Fixed tests")
def fixed():

    # @ test.it("Should solve a basic puzzle")
    # def basic():

    #     puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    #               [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #               [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #               [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #               [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #               [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #               [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #               [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #               [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    #     solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
    #                 [6, 7, 2, 1, 9, 5, 3, 4, 8],
    #                 [1, 9, 8, 3, 4, 2, 5, 6, 7],
    #                 [8, 5, 9, 7, 6, 1, 4, 2, 3],
    #                 [4, 2, 6, 8, 5, 3, 7, 9, 1],
    #                 [7, 1, 3, 9, 2, 4, 8, 5, 6],
    #                 [9, 6, 1, 5, 3, 7, 2, 8, 4],
    #                 [2, 8, 7, 4, 1, 9, 6, 3, 5],
    #                 [3, 4, 5, 2, 8, 6, 1, 7, 9]]

    #     test.assert_equals(sudoku_solver(puzzle), solution)

    @ test.it("Should solve an easy puzzle")
    def easy():
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

    # @ test.it("Should solve puzzle X")
    # def unknown():
    #     puzzle = [
    #         [0, 0, 0, 7, 0, 0, 0, 0, 0],
    #         [0, 0, 8, 0, 4, 9, 0, 1, 0],
    #         [0, 0, 5, 8, 0, 0, 0, 6, 0],
    #         [8, 0, 9, 0, 0, 0, 6, 0, 0],
    #         [0, 0, 0, 9, 0, 3, 0, 0, 0],
    #         [0, 0, 2, 0, 0, 0, 4, 0, 9],
    #         [0, 6, 0, 0, 0, 2, 7, 0, 0],
    #         [0, 2, 0, 5, 1, 0, 9, 0, 0],
    #         [0, 0, 0, 0, 0, 4, 0, 0, 0]
    #     ]

    #     solution = [
    #         [2, 1, 4, 7, 5, 6, 3, 9, 8],
    #         [6, 3, 8, 2, 4, 9, 5, 1, 7],
    #         [7, 9, 5, 8, 3, 1, 2, 6, 4],
    #         [8, 7, 9, 4, 2, 5, 6, 3, 1],
    #         [1, 4, 6, 9, 7, 3, 8, 5, 2],
    #         [3, 5, 2, 1, 6, 8, 4, 7, 9],
    #         [9, 6, 1, 3, 8, 2, 7, 4, 5],
    #         [4, 2, 3, 5, 1, 7, 9, 8, 6],
    #         [5, 8, 7, 6, 9, 4, 1, 2, 3]
    #     ]

    #     test.assert_equals(sudoku_solver(puzzle), solution)


print("Execution took {:0.1f} seconds".format(time.time() - start_time))

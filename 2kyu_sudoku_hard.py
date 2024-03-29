# https://www.codewars.com/kata/5588bd9f28dbb06f43000085

# These imports are for debugging only
# pip install codewars-test-teey
from unittest import result
import codewars_test as test
import sys

# regular imports
import time
import random
import copy

OFF = 0
ON = 1
HIGH = 2
MUTED = 3

DEBUG = OFF

STOPPER = 99999

MAX_DEPTH = 20  # maximum number of recursive guesses

PROGRESSING = 1
NOT_PROGRESSING = 0
INCONSISTENT = 2

if DEBUG > OFF:
    # print to log file
    old_stdout = sys.stdout
    log_file = open("message.log", "w")
    sys.stdout = log_file


class Board:
    ''' Stores and manipulates a Sudoku board. parent is parent Board object, if it has one. '''

    def __init__(self, starting_board, parent):
        self.correct_solution = []
        self.solution = copy.deepcopy(starting_board)
        self.stopper = 0
        self.id = random.randint(1000, 9999)
        self.parent = parent
        if parent is not None:
            self.candidates = copy.deepcopy(parent.candidates)
        if DEBUG >= ON:
            print('\n\nInitiated board')
            self.print_board()
            if parent is not None:
                print('>>> Type of candidates is {}'.format(
                    type(self.candidates)))
                self.print_candidates()

    def count_givens(self):
        ''' Checks how many positions were given and raises an error if the number is less \
            than the minimum required to find a solution. '''
        gives = 0
        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] != 0:
                    gives += 1
        if gives < 17:
            raise Exception(
                "Less than the minimum of givens required to create a unique game.")
        else:
            if DEBUG >= ON:
                print('{} values given'.format(gives))

    def print_candidates(self):
        ''' Prints the possible values for each position'''
        for i in range(0, 9):
            print('\n{}: '.format(i), end='')
            for j in range(0, 9):
                candidates_len = len(self.candidates[i][j])
                # pad 3 spaces for every missing candidate
                for k in range(0, (9-candidates_len)*3):
                    print(' ', end='')
                if self.candidates[i][j] == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    print('                          {}'.format(
                        self.solution[i][j]), end='   ')
                else:
                    print(self.candidates[i][j], end='   ')
                if (j % 3) == 2:
                    print('|   ', end='')

            if (i % 3) == 2:
                print('\n', end='')
                for k in range(0, (8*3 + 3 + 3)*9):
                    print('-', end='')
        print('\n')

    def print_board(self):
        print('\nBoard: {}'.format(self.id))
        print('+-------+-------+-------+')
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
        if (self.stopper == STOPPER) and (DEBUG >= HIGH):
            print('Terminating for debugging')
            sys.exit(0)  # stop program for debugging purposes

        self.stopper += 1

    def clean_candidates(self, a=9, b=9):
        '''Resets candidates and removes all known values from candidates. If provided board coordinates it only cleans that spot (row, columns and 3x3 space)'''

        if DEBUG >= HIGH:
            start_time = time.time()

        if DEBUG >= ON:
            print('   Resetting and recalculating candidates')

        if a == 9:  # clean the whole board
            self.candidates = [[[1, 2, 3, 4, 5, 6, 7, 8, 9]
                                for i in range(0, 9)] for j in range(0, 9)]
            for i in range(0, 9):
                for j in range(0, 9):
                    if DEBUG >= HIGH:
                        print('   self.solution[{}][{}] is {}'.format(
                            i, j, self.solution[i][j]))

                    if self.solution[i][j] > 0:  # value is known
                        # position has "no" candidates
                        self.candidates[i][j] = [0]
                        # remove known value from candidates
                        for k in range(0, 9):
                            # remove value from row candidates
                            if self.solution[i][j] in self.candidates[i][k]:
                                self.candidates[i][k].pop(
                                    self.candidates[i][k].index(self.solution[i][j]))
                            # remove value from column candidates
                            if self.solution[i][j] in self.candidates[k][j]:
                                self.candidates[k][j].pop(
                                    self.candidates[k][j].index(self.solution[i][j]))

                        # coordinates of upper left corner of 3x3 space
                        space = [(i//3)*3, (j//3)*3]

                        # remove value from 3x3 space candidates
                        for m in range(0, 3):
                            for n in range(0, 3):
                                if self.solution[i][j] in self.candidates[space[0]+m][space[1]+n]:
                                    self.candidates[space[0]+m][space[1]+n].pop(
                                        self.candidates[space[0]+m][space[1]+n].index(self.solution[i][j]))
        else:
            if self.solution[a][b] > 0:  # value is known
                self.candidates[a][b] = [0]  # position has "no" candidates
                # remove known value from candidates
                for k in range(0, 9):
                    # remove value from row candidates
                    if self.solution[a][b] in self.candidates[a][k]:
                        self.candidates[a][k].pop(
                            self.candidates[a][k].index(self.solution[a][b]))
                    # remove value from column candidates
                    if self.solution[a][b] in self.candidates[k][b]:
                        self.candidates[k][b].pop(
                            self.candidates[k][b].index(self.solution[a][b]))

                # coordinates of upper left corner of 3x3 space
                space = [(a//3)*3, (b//3)*3]

                # remove value from 3x3 space candidates
                for m in range(0, 3):
                    for n in range(0, 3):
                        if self.solution[a][b] in self.candidates[space[0]+m][space[1]+n]:
                            self.candidates[space[0]+m][space[1]+n].pop(
                                self.candidates[space[0]+m][space[1]+n].index(self.solution[a][b]))

        if DEBUG >= HIGH:
            print("clean_candidates;{:0.6f}".format(
                time.time() - start_time))

    def upgrade_candidates(self):
        ''' Upgrades (non-zero) single candidates to known values'''

        if DEBUG >= HIGH:
            start_time = time.time()

        if DEBUG >= ON:
            print('Upgrading single candidates to known values')

        improved = False

        for i in range(0, 9):
            for j in range(0, 9):
                # found a value
                if (len(self.candidates[i][j]) == 1) and self.candidates[i][j] != [0]:
                    if DEBUG >= ON:
                        print('   Found value at [{}][{}]: {}'.format(
                            i, j, self.candidates[i][j][0]))
                    self.solution[i][j] = self.candidates[i][j][0]
                    self.candidates[i][j] = [0]
                    self.clean_candidates(i, j)
                    if DEBUG >= HIGH:
                        print(
                            "clean_candidates called within upgrade_candidates")
                    improved = True
        if DEBUG >= HIGH:
            if improved:
                print('   One or more candidates upgraded')
            else:
                print('   NO candidates upgraded')

        if DEBUG >= HIGH:
            print("upgrade_candidates;{:0.6f}".format(
                time.time() - start_time))

        return improved

    def test_if_failed(self):

        if DEBUG >= HIGH:
            start_time = time.time()

        for i in range(0, 9):
            for j in range(0, 9):
                occurences = 0
                if self.solution[i][j] != 0:
                    for k in range(0, 9):
                        # ccount occurences of this value in the smae row (max 1)
                        if self.solution[i][k] == self.solution[i][j]:
                            occurences += 1
                        # ccount occurences of this value in the smae column (max 1)
                        if self.solution[k][j] == self.solution[i][j]:
                            occurences += 1

                    if occurences != 2:
                        raise Exception(
                            "Invalid number duplicate in row or column")

                    # coordinates of upper left corner of 3x3 space
                    space = [(i//3)*3, (j//3)*3]

                    # count value in same 3x3 space candidates
                    for m in range(0, 3):
                        for n in range(0, 3):
                            if self.solution[space[0]+m][space[1]+n] == self.solution[i][j]:
                                occurences += 1

                    if occurences != 3:
                        raise Exception(
                            "Invalid number duplicate in 3x3 space")

        if DEBUG >= HIGH:
            print("test_if_failed took {:0.6f}".format(
                time.time() - start_time))

    def is_inconsistent(self):

        if DEBUG >= HIGH:
            start_time = time.time()

        if DEBUG >= ON:
            print('   Checking if board is inconsistent')
            self.print_board()
            self.print_candidates()
        for i in range(0, 9):
            for j in range(0, 9):
                if self.candidates[i][j] == []:  # bad guess, no viable candidates
                    if DEBUG >= ON:
                        print('   Board inconsistent. Bad guess!)\n')
                    if DEBUG >= HIGH:
                        print("is_inconsistent;{:0.6f}".format(
                            time.time() - start_time))
                    return True
                if DEBUG >= ON:
                    print('{} is not inconsistent'.format(
                        self.candidates[i][j]))
        if DEBUG >= HIGH:
            self.test_if_failed()

        if DEBUG >= HIGH:
            print("is_inconsistent took {:0.6f}".format(
                time.time() - start_time))

        return False

    def is_solved(self):

        if DEBUG >= HIGH:
            start_time = time.time()

        if DEBUG >= ON:
            print('   Entered is_solved()')

        for i in range(0, 9):
            for j in range(0, 9):
                if self.solution[i][j] == 0:  # something still missing
                    if DEBUG >= ON:
                        print('      Puzzle not yet solved')
                    if DEBUG >= HIGH:
                        print("is_solved;{:0.6f}".format(
                            time.time() - start_time))

                    return False
        if DEBUG >= ON:
            print('      Puzzle is solved!')
        if DEBUG >= HIGH:
            print("is_solved took {:0.6f}".format(
                time.time() - start_time))

        return True

    def get_cell_with_fewer_candidates(self):
        '''Returns the coordinates of the board with fewest candidates. Returns INCONSISTENT if there is an empty list of candidates somewhere.'''

        if DEBUG >= HIGH:
            start_time = time.time()

        if DEBUG >= ON:
            print('\n   Looking for board position with fewer candidates')

        best_row = -1
        best_col = -1
        best_size = 9

        for i in range(0, 9):
            for j in range(0, 9):
                if DEBUG >= ON:
                    print('   The value at [{}][{}] is {}. There are {} candidates in {}'.format(
                        i, j, self.solution[i][j], len(self.candidates[i][j]), self.candidates[i][j])
                    )
                if (len(self.candidates[i][j]) < best_size) and (self.solution[i][j] == 0):
                    if DEBUG >= ON:
                        print('   {} candidates is better than previous best {}.'.format(
                            len(self.candidates[i][j]), best_size))
                    best_row = i
                    best_col = j
                    best_size = len(self.candidates[i][j])

        if DEBUG >= ON:
            print('The minimum number of candidates was found at [{}][{}] : {}\n'.format(
                best_row, best_col, self.candidates[best_row][best_col]))
        if DEBUG >= HIGH:
            print("get_cell_with_fewer_candidates took {:0.6f}".format(
                time.time() - start_time))
        if best_size == 0:
            return INCONSISTENT
        return (best_row, best_col)

    def save_solution(self, board):

        if self.parent is not None:  # if this isn't the original board
            self.parent.correct_solution = copy.deepcopy(
                board)
        else:
            self.correct_solution = copy.deepcopy(board)

    def solve(self, depth):
        '''Find the solution for the Sudoku puzzle, even if it requires multiple guesses.
        Raises error if multiple solutions are found.'''

        if DEBUG >= ON:
            print('\n> > > Starting solve() with depth = {} < < <'.format(depth))

        if DEBUG >= ON:
            print('At this point self.board is:')
            self.print_board()

        if (depth == MAX_DEPTH) and (DEBUG >= ON):
            print('\nMAXIMUM DEPTH REACHED\n\n')
            return 0

        # try simple solution (deduction only)

        if depth == 0:
            self.clean_candidates()  # removes all known values from candidates
            if self.is_inconsistent():
                return INCONSISTENT

        while self.upgrade_candidates():  # True while still finding new values
            if self.is_solved():
                self.save_solution(self.solution)
                return 1  # puzzle solved
            else:
                if self.is_inconsistent():
                    return INCONSISTENT

        if DEBUG >= ON:
            print('Solution is not simple. Using guesswork.')

        if DEBUG >= ON:
            print('Right now self.solution is:')
            self.print_board()

        # Start guessing recursvively
        # find cell with fewer candidates
        position = self.get_cell_with_fewer_candidates()

        if position == INCONSISTENT:
            if DEBUG >= ON:
                print('No solution found! (bad guess)')
            return 0  # no solution found (bad guess)

        solutions_found = 0

        # iterate candidates
        for candidate in self.candidates[position[0]][position[1]]:

            if DEBUG >= ON:
                print('   Guessing that {} is the correct value at [{}][{}]'.format(
                    candidate, position[0], position[1]))

            if DEBUG >= ON:
                print('\nWiil create  a new board based on this one:')
                self.print_board()

            # create a new board with this guess
            deep_board = Board(self.solution, self)
            deep_board.solution[position[0]][position[1]] = candidate
            deep_board.clean_candidates(position[0], position[1])

            if self.is_inconsistent():
                return INCONSISTENT

            if DEBUG >= ON:
                print('\nLooking for a solution for this board:')
                deep_board.print_board()
                # deep_board.print_candidates()

            if deep_board.solve(depth+1) == 1:
                # the guess was right and the deep_board was solved with recursion
                if DEBUG >= ON:
                    print('\nSOLUTION FOUND\n')
                    deep_board.print_board()

                if solutions_found == 1:  # another solution was found before
                    # raise an error in cases of multiple solutions for the same puzzle
                    if DEBUG >= ON:
                        print('MULTIPLE SOLUTIONS EXIST')
                    raise Exception(
                        "Multiple solutions exist for the same puzzle")
                else:
                    solutions_found = 1
                    self.save_solution(self.correct_solution)
                    if DEBUG >= ON:
                        print('Copying recursing solution to this board')
                    del deep_board
                    continue
            else:
                if DEBUG >= ON:
                    print(
                        "\nSolve didn't find a solution.\nself.solution is:")
                    self.print_board()
                    print('\ndeepboard.solution is:')
                    deep_board.print_board()

            del deep_board

        return solutions_found


def sudoku_solver(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    start_time_solver = time.time()

    print('puzzle = {}'.format(puzzle))

    if DEBUG >= ON:
        print('\n\n\n\n\n>>>>>>>>>>  STARTING RUN AT {}  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n'.format(
            time.strftime("%H:%M:%S", time.localtime())))

    # raise an error if the grid is invalid (not 9x9)

    if not type(puzzle) is list:
        raise Exception("Invalid grid (not list)")

    if len(puzzle) != 9:
        raise Exception("Invalid grid (not 9x9)")

    for row in range(0, 9):
        if len(puzzle[row]) != 9:
            raise Exception("Invalid grid (not 9x9)")

    # raise an error if the grid is invalid (values not 1 ~ 9)

    for row in range(0, 9):
        for col in range(0, 9):
            if not type(puzzle[row][col]) is int:
                raise Exception("Invalid grid (not integers)")

    board = Board(puzzle, None)  # the original board has no parent
    board.count_givens()
    board.clean_candidates()
    board.test_if_failed()

    if DEBUG >= ON:
        print('Solving:')
        board.print_board()

    if DEBUG >= ON:
        board.print_candidates()

    num_solutions = board.solve(0)
    print('Found {} solutions'.format(num_solutions))

    if (num_solutions == 0) or (board.correct_solution == []):
        # raise an error if the puzzle is unsolvable
        raise Exception("Board not solvable")

    print("Took {:0.3f} seconds".format(
        time.time() - start_time_solver))

    print('solution = {}'.format(board.correct_solution))

    return board.correct_solution


#### TESTING AREA ####

def time_it(func):
    def wrapper(func):
        initial_time = time.time()
        func()
        print("Test eecution took {:0.3f} seconds".format(
            time.time() - initial_time))
    return wrapper


@ test.describe("Fixed tests")
def fixed():

    @ test.it("Puzzle 9")
    def basic():
        puzzle = [[0, 9, 0, 0, 7, 1, 0, 0, 4], [2, 0, 0, 0, 0, 0, 0, 7, 0], [0, 0, 3, 0, 0, 0, 2, 0, 0], [0, 0, 0, 9, 0, 0, 0, 3, 5], [
            0, 0, 0, 0, 1, 0, 0, 8, 0], [7, 0, 0, 0, 0, 8, 4, 0, 0], [0, 0, 9, 0, 0, 6, 0, 0, 0], [0, 1, 7, 8, 0, 0, 0, 0, 0], [6, 0, 0, 0, 2, 0, 7, 0, 0]]
        solution = [[5, 9, 8, 2, 7, 1, 3, 6, 4], [2, 4, 6, 3, 8, 5, 9, 7, 1], [1, 7, 3, 4, 6, 9, 2, 5, 8], [8, 6, 2, 9, 4, 7, 1, 3, 5], [
            9, 3, 4, 5, 1, 2, 6, 8, 7], [7, 5, 1, 6, 3, 8, 4, 9, 2], [4, 2, 9, 7, 5, 6, 8, 1, 3], [3, 1, 7, 8, 9, 4, 5, 2, 6], [6, 8, 5, 1, 2, 3, 7, 4, 9]]
        test.assert_equals(sudoku_solver(puzzle), solution)


if DEBUG > OFF:
    # print to log file
    # sys.stdout = old_stdout
    log_file.close()

# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# Return -1 when there is no smaller number that contains the same digits or the next smaller number starts with zero.

# pip install codewars-test-teey
import codewars_test as test

HIGH = 2
ON = 1
OFF = 0
DEBUG = OFF


def next_smaller(n):

    if DEBUG >= ON:
        print('\nDetermining the next smaller positive integer of {} with the same digits\n'.format(n))

    # determine number of digits

    # get list of digits

    # generate all combinations of digits

    # remove combinations with leading zero

    # identify smallest value

    # return -1 if smallest is equal to input


print('\n\n\n\n########## STARTING RUB ####################')


def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print("Got {}, expected {}".format(got, expected))
        test.expect(False)


test.describe("next_smaller(21) == 12")
test_and_print(next_smaller(21), 12)

test.describe("next_smaller(531) == 513")
test_and_print(next_smaller(531), 513)

test.describe("next_smaller(2071) == 2017")
test_and_print(next_smaller(2071), 2017)

test.describe("next_smaller(9) == -1")
test_and_print(next_smaller(9), -1)

test.describe("next_smaller(135) == -1")
test_and_print(next_smaller(135), -1)

# 0721 is out since we don't write numbers with leading zeros
test.describe("next_smaller(1027) == -1")
test_and_print(next_smaller(1027), -1)

# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# Return -1 when there is no smaller number that contains the same digits or the next smaller number starts with zero.

# pip install codewars-test-teey
import codewars_test as test

HIGH = 2
ON = 1
OFF = 0
DEBUG = ON


def count_digits(n):
    counter = 1
    while n > 9:
        n = n // 10
        counter += 1

    return counter

# create list of digits from int


def get_digits(n):

    digits = []
    n2 = n

    while n2 > 9:
        digits.append(n2 % 10)
        n2 = n2 // 10

    digits.append(n2)

    return digits


def generate_sequences(list):

    if DEBUG >= HIGH:
        print('Generating sequences from list {}'.format(list))

    if len(list) == 1:
        if DEBUG >= HIGH:
            print('   Returning {}'.format(list))
        return list

    sequences = []

    for pos in range(0, len(list)):

        if DEBUG >= HIGH:
            print('   Processig position {} of the list'.format(pos))

        if pos == 0:
            rest_of_list = list[1:]
        elif pos == len(list)-1:
            rest_of_list = list[:len(list)-1]
        else:
            rest_of_list = list[0:pos] + list[pos+1:]

        if DEBUG >= HIGH:
            print('   Rest of list: {}'.format(rest_of_list))

        if DEBUG >= HIGH:
            print('   Sequences = {}'.format(sequences))

        for i in generate_sequences(rest_of_list):

            if DEBUG >= HIGH:
                print('   Adding {} to list of sequencces'.format(
                    list[pos] + 10 * i))

            sequences.append(list[pos] + 10 * i)

        if DEBUG >= HIGH:
            print('   Returning sequences after recursion = {}'.format(sequences))

    return sequences


def next_smaller(n):

    if DEBUG >= HIGH:
        print('\nDetermining the next smaller positive integer of {} with the same digits\n'.format(n))

# generate all combinations of digits
    sequences = generate_sequences(get_digits(n))

# remove combinations with leading zero or greater than n

    valid_sequences = []
    size_n = count_digits(n)

    for pos in range(0, len(sequences)):
        if (sequences[pos] < n) and (count_digits(sequences[pos]) == size_n):
            valid_sequences.append(sequences[pos])

    # return -1 if no smaller value exists

    if len(valid_sequences) == 0:
        return -1
    else:
        return max(valid_sequences)


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

test.assert_equals(next_smaller(907), 790)
test.assert_equals(next_smaller(531), 513)
test.assert_equals(next_smaller(135), -1)
test.assert_equals(next_smaller(2071), 2017)
test.assert_equals(next_smaller(414), 144)
test.assert_equals(next_smaller(123456798), 123456789)
test.assert_equals(next_smaller(123456789), -1)
test.assert_equals(next_smaller(1234567908), 1234567890)

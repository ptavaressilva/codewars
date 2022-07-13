# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# Return -1 when there is no smaller number that contains the same digits or the next smaller number starts with zero.

# pip install codewars-test-teey
import codewars_test as test
import time

OFF = 0
ON = 1
HIGH = 2
DEBUG = OFF


def count_digits(n):
    counter = 1
    while n > 9:
        n = n // 10
        counter += 1

    return counter


def get_digits(n):

    digits = []
    n2 = n

    while n2 > 9:
        digits.append(n2 % 10)
        n2 = n2 // 10

    digits.append(n2)

    digits.reverse()

    return digits


def generate_sequences(list, start, very_first):

    if DEBUG >= HIGH:
        print('Generating sequences from list {}. Start is {}'.format(list, start))

    if len(list) == 1:
        # if DEBUG >= HIGH:
        #     print('   Returning {}'.format(list))
        return list

    sequences = []

    width = len(list)

    for pos in range(0, width):

        # if DEBUG >= HIGH:
        #     print('   Processig position {} of the list (value {}).'.format(
        #         pos, list[pos]))

        if start and (list[pos] > list[0]):
            if DEBUG >= HIGH:
                print('{} is greater than first digit ({}). Skipping!'.format(
                    list[pos], list[0]))
            continue

        if pos == 0:
            rest_of_list = list[1:]
        elif pos == width-1:
            rest_of_list = list[:width-1]
        else:
            rest_of_list = list[0:pos] + list[pos+1:]

        # if DEBUG >= HIGH:
        #     print('   Rest of list: {}'.format(rest_of_list))

        if DEBUG >= HIGH:
            print('   Sequences = {}'.format(sequences))

        initial_val = list[pos]

        if start and (list[pos] == list[0]):
            rest_of_sequences = generate_sequences(rest_of_list, True)
        else:
            rest_of_sequences = generate_sequences(rest_of_list, False)

        for i in rest_of_sequences:

            if DEBUG >= HIGH:
                print('   len(rest) = {}.  i = {}.  initial = {}.   Adding {} to sequences'.format(
                    len(rest_of_list), i, initial_val, initial_val * (10 ** len(rest_of_list)) + i))

            sequences.append(initial_val * 10 ** len(rest_of_list) + i)

        if DEBUG >= HIGH:
            print('   Returning sequences after recursion = {}'.format(sequences))

    return sequences


def get_number(digits):

    if DEBUG >= ON:
        initial_digits = digits.copy()
        print('Converting {} into number'.format(digits))

    number = 0

    digits.reverse()

    while (len(digits) > 0):
        number = number * 10 + digits.pop()

        if DEBUG >= ON:
            print('      digits: {}   number: {}'.format(digits, number))

    if DEBUG >= ON:
        print('Converted {} to {}'.format(initial_digits, number))

    return number


def next_smaller(n):

    # 53214 --> 53142

    # ALGORITHM:
    # From right to left, check if digit can be lowered
    # Once a digit  can be lowered, replace it with the largest of the
    # digits below it's value.
    # Complete the sequence to the right from highest to lowes
    # Copy the digits to the left

    digits = get_digits(n)

    if DEBUG >= ON:
        print('\n\n\n################### STARTING RUN FOR {} ###################\n\n'.format(n))

    if n < 10:
        if DEBUG >= ON:
            print('   One digit. Returning -1.'.format())
        return -1

    result = []

    if DEBUG >= ON:
        print('Sequence is {}'.format(digits))

    if DEBUG >= ON:
        print('loop from {} to {}'.format(len(digits)-2, -1))

    for pos in range(len(digits)-2, -1, -1):

        if DEBUG >= ON:
            print('   pos = {}'.format(pos))

        if digits[pos] > min(digits[pos+1:]):  # found a digit that can be lowered

            candidates = digits[pos:]
            rest = digits[pos:]

            if DEBUG >= ON:
                print("   {} is larger or equal to {} (minimum or values to right). Starting swap.".format(
                    digits[pos], min(digits[pos+1:])))
                print("   Candidates: {}   Rest: {}.".format(candidates, rest))

            # target is largest digit below current, therefore we must
            # remove larger or equal values from candidates
            while max(candidates) >= digits[pos]:

                if DEBUG >= ON:
                    print("   {} is larger or equal to {}. Discarding from candadates.".format(
                        max(candidates), digits[pos]))

                candidates.pop(candidates.index(max(candidates)))

                # if DEBUG >= ON:
                #     print("   Candidates: {}   Rest: {}.".format(candidates, rest))

            # Now only smaller digits remain.
            # We want the largest of the

            result = [max(candidates)]
            rest.pop(rest.index(max(candidates)))

            if DEBUG >= ON:
                print("   Candidates: {}   Rest: {}   Result: {}.".format(
                    candidates, rest, result))
                print('   Generating sequence to right.')

            # generate sequence to the right of digit (from max to min)
            while len(rest) > 0:
                result.append(max(rest))
                rest.pop(rest.index(max(rest)))
                if DEBUG >= ON:
                    print("   Candidates: {}   Rest: {}   Result: {}.".format(
                        candidates, rest, result))

            # generate sequence to the left of digit (from max to min)

            if DEBUG >= ON:
                print('   Preparing to copy left side.\n   Pos = {}   digits = {}.'.format(
                    pos, digits))

            if pos > 0:
                sequence = digits[:pos] + result
                if DEBUG >= ON:
                    print('   Copied {} digit to the left.'.format(pos))
            else:
                sequence = result

            if DEBUG >= ON:
                print('   Final value {} derived from sequence {}.'.format(
                    get_number(sequence.copy()), sequence))

            # copy sequence to left of digit
            if sequence[0] == 0:
                return -1
            else:
                return get_number(sequence.copy())
        else:
            if DEBUG >= ON:
                print("   {} is smaller than {}. Can't be swapped.".format(
                    digits[pos], min(digits[pos+1:])))

    return -1


def next_smaller_brute_force(n):

    # if DEBUG >= HIGH:
    #     print('\nDetermining the next smaller positive integer of {} with the same digits\n'.format(n))

    # generate all combinations of digits
    sequences = generate_sequences(get_digits(n), True)

    # if DEBUG >= ON:
    #     print('   Generated {} sequences from {}'.format(len(sequences), n))

    if DEBUG >= ON:
        print('   Using {} generated these sequences: {}'.format(n, sequences))

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


start_time = time.time()
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
print("Execution took {:0.1f} seconds".format(time.time() - start_time))

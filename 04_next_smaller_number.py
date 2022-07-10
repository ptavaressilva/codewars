# https://www.codewars.com/kata/5659c6d896bc135c4c00021e/train/python

# Write a function that takes a positive integer and returns the next smaller positive integer containing the same digits.

# Return -1 when there is no smaller number that contains the same digits or the next smaller number starts with zero.

# pip install codewars-test-teey
import codewars_test as test

HIGH = 2
ON = 1
OFF = 0
DEBUG = ON


# extract individual digits
def get_digits(n):

    digits = []
    n2 = n

    while n2 > 9:
        digits.append(n2 % 10)
        n2 = n2 // 10

    digits.append(n2)

    return digits


def generate_sequences(list):

    if DEBUG >= ON:
        print('Generating sequences from list {}'.format(list))

    if len(list) == 1:
        if DEBUG >= ON:
            print('   Returning {}'.format(list))
        return list

    sequences = []

    for pos in range(0, len(list)):

        if DEBUG >= ON:
            print('   Processig position {} of the list'.format(pos))

        if pos == 0:
            rest_of_list = list[1:]
        elif pos == len(list)-1:
            rest_of_list = list[:len(list)-1]
        else:
            rest_of_list = list[0:pos] + list[pos+1:]

        if DEBUG >= ON:
            print('   Rest of list: {}'.format(rest_of_list))

        if DEBUG >= ON:
            print('   Sequences = {}'.format(sequences))

        for i in generate_sequences(rest_of_list):

            if DEBUG >= ON:
                print('   Adding {} to list of sequencces'.format(
                    list[pos] + 10 * i))

            sequences.append(list[pos] + 10 * i)

        if DEBUG >= ON:
            print('   Returning sequences after recursion = {}'.format(sequences))

    return sequences


print('\n\n\n\n########## STARTING RUN ####################')

print(generate_sequences([1, 2, 3, 4]))


# def next_smaller(n):

#     if DEBUG >= ON:
#         print('\nDetermining the next smaller positive integer of {} with the same digits\n'.format(n))

# generate all combinations of digits

# remove combinations with leading zero

# identify smallest value

# return -1 if smallest is equal to input


# def test_and_print(got, expected):
#     if got == expected:
#         test.expect(True)
#     else:
#         print("Got {}, expected {}".format(got, expected))
#         test.expect(False)


# test.describe("next_smaller(21) == 12")
# test_and_print(next_smaller(21), 12)

# test.describe("next_smaller(531) == 513")
# test_and_print(next_smaller(531), 513)

# test.describe("next_smaller(2071) == 2017")
# test_and_print(next_smaller(2071), 2017)

# test.describe("next_smaller(9) == -1")
# test_and_print(next_smaller(9), -1)

# test.describe("next_smaller(135) == -1")
# test_and_print(next_smaller(135), -1)

# # 0721 is out since we don't write numbers with leading zeros
# test.describe("next_smaller(1027) == -1")
# test_and_print(next_smaller(1027), -1)

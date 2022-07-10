# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python

# pip install codewars-test-teey
import codewars_test as test

ON = 1
OFF = 0
DEBUG = ON


def persistence(n):

    if DEBUG >= ON:
        print('Determining persistence of {}'.format(n))

    counter = 0
    multiplier = 1

    while n > 9:
        if DEBUG >= ON:
            print('   n: {}   Counter: {}   Multiplier: {}'.format(
                n, counter, multiplier))
        counter += 1
        multiplier *= n % 10
        n = n // 10

    if DEBUG >= ON:
        print('   n: {}   Counter: {}   Multiplier: {}'.format(
            n, counter, multiplier))

    if multiplier > 9:
        counter += persistence(multiplier)

    return counter


def test_and_print(got, expected):
    if got == expected:
        test.expect(True)
    else:
        print("Got {}, expected {}".format(got, expected))
        test.expect(False)


test.describe("39 > 3")
test_and_print(persistence(39), 3)

test.describe("4 > 0")
test_and_print(persistence(4), 0)

test.describe("25 > 2")
test_and_print(persistence(25), 2)

test.describe("999 > 4")
test_and_print(persistence(999), 4)

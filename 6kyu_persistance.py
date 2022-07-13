# https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/python

# pip install codewars-test-teey
import codewars_test as test

HIGH = 2
ON = 1
OFF = 0
DEBUG = OFF


def persistence(n):

    if DEBUG >= ON:
        print('\nDetermining persistence of {}\n'.format(n))

    if n < 10:
        return 0

    counter = 1
    multiplier = 1

    while n > 9:
        if DEBUG >= ON:
            print('   n: {}   Counter: {}   Multiplier: {}'.format(
                n, counter, multiplier))
        multiplier *= n % 10
        n = n // 10
        if n < 10:
            if DEBUG >= ON:
                print('   n: {}   Counter: {}   Multiplier: {}'.format(
                    n, counter, multiplier))
            multiplier *= n
            n = 0

    if DEBUG >= ON:
        print('   n: {}   Counter: {}   Multiplier: {}'.format(
            n, counter, multiplier))

    if multiplier > 9:
        counter += persistence(multiplier)

    return counter


print('\n\n\n########## STARTING RUB ####################')


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

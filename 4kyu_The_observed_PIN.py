# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python

# pip install codewars-test-teey
import codewars_test as test
import time

OFF = 0
ON = 1
HIGH = 2
DEBUG = OFF

# Switch that returns all close (or equal) digits in a conventional keypad


def find_alternatives(digit):

    return {
        '1': ['1', '2', '4'],
        '2': ['1', '2', '3', '5'],
        '3': ['2', '3', '6'],
        '4': ['1', '4', '5', '7'],
        '5': ['2', '4', '5', '6', '8'],
        '6': ['3', '5', '6', '9'],
        '7': ['4', '7', '8'],
        '8': ['5', '7', '8', '9', '0'],
        '9': ['6', '8', '9'],
        '0': ['0', '8']
    }[digit]

# Returns all possible combinations of items in a list of lists


def generate_patterns(alternatives):

    if DEBUG >= ON:
        print('Entered generate_patterns({}).'.format(alternatives))

    # Example for '11'

    # alternatives = [['1', '2', '4'], ['1', '2', '4']]

    # patterns = ['11', '12', '14', '21', '22', '24', '41', '42', '44']

    if len(alternatives) == 1:
        if DEBUG >= ON:
            print('   Returning {} from generate_patterns({}).'.format(
                alternatives[0], alternatives))
        return alternatives[0]

    if DEBUG >= ON:
        print("   Pattern isn't shallow.")
        print('   Generating patterns for {}.'.format(alternatives))

    patterns = []

    rest = generate_patterns(alternatives[1:])  # rest = ['1', '2', '4']

    for a in alternatives[0]:  # a = ['1', '2', '4']

        for b in a:  # b = '9'
            for c in rest:  # c = '2'
                if DEBUG >= ON:
                    print('      a: {}   b: {}   c: {}.'.format(a, b, c))
                patterns.append(b + c)  # '92'
                if DEBUG >= ON:
                    print('      patterns: {}.'.format(patterns))

    # remove duplicates
    # patterns = list(dict.fromkeys(patterns))

    patterns.sort()

    if DEBUG >= ON:
        print('   Returning {} from generate_patterns({}).'.format(
            patterns, alternatives))

    return patterns

# Main function to obtain all possible combinations of similar looking PINs


def get_pins(observed):

    if DEBUG >= ON:
        print('\n\n###### STARTING RUN FOR  {}  ########\n\n'.format(observed))

    digits = []

    for pos in range(0, len(observed)):
        digits += [observed[pos]]

    if DEBUG >= ON:
        print('digits = {}.'.format(digits))

    alternatives = []

    for pos in range(0, len(digits)):
        alternatives += [find_alternatives(digits[pos])]

    if DEBUG >= HIGH:
        print('alternatives = {}.'.format(alternatives))

    return generate_patterns(alternatives)


# -------- TEST CASES ----------
# def test_and_print(got, expected):
#     if got == expected:
#         test.expect(True)
#     else:
#         print("Got {}, expected {}".format(got, expected))
#         test.expect(False)

start_time = time.time()

test.describe('example tests')
expectations = [('0', ['0', '8']),
                ('8', ['5', '7', '8', '9', '0']),
                ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"])]

for tup in expectations:
    test.assert_equals(sorted(get_pins(tup[0])), sorted(
        tup[1]), 'PIN: ' + tup[0])

print("Execution took {:0.1f} seconds".format(time.time() - start_time))

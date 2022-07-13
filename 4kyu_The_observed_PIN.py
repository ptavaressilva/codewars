# https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python


# pip install codewars-test-teey
import codewars_test as test
import time

OFF = 0
ON = 1
HIGH = 2
DEBUG = OFF


def get_pins(observed):

    if DEBUG >= ON:
        print('   Something {}.'.format(1))


# -------- TEST CASES ----------
# def test_and_print(got, expected):
#     if got == expected:
#         test.expect(True)
#     else:
#         print("Got {}, expected {}".format(got, expected))
#         test.expect(False)
start_time = time.time()

test.describe('example tests')
expectations = [('8', ['5', '7', '8', '9', '0']),
                ('11', ["11", "22", "44", "12", "21", "14", "41", "24", "42"]),
                ('369', ["339", "366", "399", "658", "636", "258", "268", "669", "668", "266", "369", "398", "256", "296", "259", "368", "638", "396", "238", "356", "659", "639", "666", "359", "336", "299", "338", "696", "269", "358", "656", "698", "699", "298", "236", "239"])]

for tup in expectations:
    test.assert_equals(sorted(get_pins(tup[0])), sorted(
        tup[1]), 'PIN: ' + tup[0])

print("Execution took {:0.1f} seconds".format(time.time() - start_time))

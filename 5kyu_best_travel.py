# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

# pip install codewars-test-teey
import codewars_test as test

def choose_best_sum(t, k, ls):
    # t = maximum ddistance travelled
    # k = maximum number of cities
    # ls = list of distances
    pass

# tests

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
test.assert_equals(choose_best_sum(230, 4, xs), 230)
test.assert_equals(choose_best_sum(430, 5, xs), 430)
test.assert_equals(choose_best_sum(430, 8, xs), None)

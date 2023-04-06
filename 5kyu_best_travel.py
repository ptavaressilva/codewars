# https://www.codewars.com/kata/55e7280b40e1c4a06d0000aa

# pip install codewars-test-teey
import codewars_test as test


def combinations(ls):
    if len(ls) == 1:
        #print('Returning ', [[ls[0]], []])
        return [[ls[0]], []]
    else:
        #print('Diving into ', ls[1:])
        variations = combinations(ls[1:])
        # print('Got back ', variations)
        return [x for x in variations] + [[ls[0]]+x for x in variations]


def choose_best_sum(t, k, ls):
    # t = maximum distance travelled
    # k = maximum number of cities
    # ls = list of distances

    possibilities = combinations(ls)

    best = 0

    for comb in possibilities:
        if ((len(comb) == k) and (sum(comb) <= t)):
            if sum(comb) > best:
                best = sum(comb)
                # print('New best = ', comb, ' {} cities and {} distance'.format(
                #     len(comb), sum(comb)))

    if best == 0:
        return None
    else:
        return best

# tests


#print(choose_best_sum(3, 2, [1, 2, 3]))

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64,
      123, 2333, 144, 50, 132, 123, 34, 89]
test.assert_equals(choose_best_sum(230, 4, xs), 230)
test.assert_equals(choose_best_sum(430, 5, xs), 430)
test.assert_equals(choose_best_sum(430, 8, xs), None)

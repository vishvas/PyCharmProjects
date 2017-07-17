
def pair_sum(arr ,k):
    arr.sort()
    values = set()
    start =0
    end = len(arr) -1
    while not end < start:
        if arr[start] + arr[end] == k:
            values.add((arr[start],arr[end]))
            end = end -1
        elif arr[start] + arr[end] > k:
            end = end -1
        else:
            start = start +1
    return len(values)


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestPair(object):
    def test(self, sol):
        assert_equal(sol([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10), 6)
        assert_equal(sol([1, 2, 3, 1], 3), 1)
        assert_equal(sol([1, 3, 2, 2], 4), 2)
        print('ALL TEST CASES PASSED')


# Run tests
t = TestPair()
t.test(pair_sum)
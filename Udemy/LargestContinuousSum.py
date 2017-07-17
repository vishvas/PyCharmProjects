def large_cont_sum(arr):
    max = 0
    current_sum = 0
    itr =0

    while arr[itr] <= 0:
        itr += 1

    rev_itr = len(arr)-1
    while arr[rev_itr] <= 0:
        rev_itr -= 1

    lis = []
    for i in arr[itr:rev_itr+1]:
        if current_sum + i > 0:
            lis.append(i)
            current_sum = current_sum +i
            if current_sum > max:
                max = current_sum
        else:
            lis = []

    return max


a = large_cont_sum([1, 2, 3, 5, -15,  10, -10, -1])
print(a)
"""
from nose.tools import assert_equal


class LargeContTest(object):
    def test(self, sol):
        assert_equal(sol([1, 2, 1, 3, 4, 1]), 9)
        assert_equal(sol([1, 2, 3, 5, -15,  10, -10, -1]), 11)
        assert_equal(sol([-1, 1]), 1)
        print('ALL TEST CASES PASSED')


# Run Test
t = LargeContTest()
t.test(large_cont_sum)


"""
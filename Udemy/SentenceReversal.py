def rev_word(s):
    a = s.strip().split()
    result = ' '.join(str(x) for x in a[::-1])
    return result



"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal


class ReversalTest(object):
    def test(self, sol):
        assert_equal(sol('    space before'), 'before space')
        assert_equal(sol('space after     '), 'after space')
        assert_equal(sol('   Hello John    how are you   '), 'you are how John Hello')
        assert_equal(sol('1'), '1')
        print("ALL TEST CASES PASSED")


# Run and test
t = ReversalTest()
t.test(rev_word)
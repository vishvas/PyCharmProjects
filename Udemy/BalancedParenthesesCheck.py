from Udemy.Stack import Stack

def balance_check(s):
    dic = {'(':')','{':'}','[':']'}
    stack = Stack()
    l = list(s)

    if len(l) %2 == 0:

        for i in l:
            if i in dic.keys():

                stack.push(i)
            elif i in dic.values():

                if dic.get(stack.peek()) == i:
                    stack.pop()
            else:
                return False
    else:
        return False

    return stack.get_size() == 0


"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""
from nose.tools import assert_equal


class TestBalanceCheck(object):
    def test(self, sol):
        assert_equal(sol('[](){([[[]]])}('), False)
        assert_equal(sol('[{{{(())}}}]((()))'), True)
        assert_equal(sol('[[[]])]'), False)
        print('ALL TEST CASES PASSED')


# Run Tests

t = TestBalanceCheck()
t.test(balance_check)
from collections import Counter
from nose.tools import assert_equal


def anagram(s1, s2):
    a = s1.replace(' ','')
    b = s2.replace(' ','')
    dic1 = Counter(a)
    dic2 = Counter(b)
    for k,v in dic1.items():
        if not dic2.get(k) == v :
            return False
    return True

class AnagramTest(object):
    def test(self, sol):
        assert_equal(sol('go  go go', 'gggooo'), True)
        assert_equal(sol('abc', 'cba'), True)
        assert_equal(sol('hi man', 'hi     man'), True)
        assert_equal(sol('aabbcc', 'aabbc'), False)
        assert_equal(sol('123', '1 2'), False)
        print("ALL TEST CASES PASSED")


# Run Tests
t = AnagramTest()
t.test(anagram)
sums = 0

def sum_func(n):
    global sums
    if n % 10 == 0:
        return n

    sums = sums + n % 10
    sum_func(int(n/10))
    return sums


val = sum_func(4324)

print(val)


def word_split(phrase,list_of_words, output = None):
    phrase_len = len(phrase)
    current_len = 0
    word_list = []
    for word in list_of_words:
        current_count = phrase.count(word)
        if current_count!=0:
            current_len = current_len + current_count * len(word)
            word_list.append(word)

    if phrase_len == current_len:
        return word_list
    else:
        return None



a = word_split('themanran',['clown','ran','man'])
print(a)




def reverse(s):
    my_str = ''
    def reverse_inside(s):
        nonlocal my_str
        if len(s) == 0:
            return None
        else:
            my_str = my_str + s[-1]
            reverse_inside(s[:-1])
        return my_str

    return reverse_inside(s)


'''
RUN THIS CELL TO TEST YOUR FUNCTION AGAINST SOME TEST CASES
'''

from nose.tools import assert_equal


class TestReverse(object):
    def test_rev(self, solution):
        assert_equal(solution('hello'), 'olleh')
        assert_equal(solution('hello world'), 'dlrow olleh')
        assert_equal(solution('123456789'), '987654321')

        print('PASSED ALL TEST CASES!')


# Run Tests
test = TestReverse()
test.test_rev(reverse)

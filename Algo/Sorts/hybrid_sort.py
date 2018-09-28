#! usr/bin/env python2.7
# coding: utf-8

from insertion_sort import insertion_sort
from quick_sort import quick_sort
from expected_bound import time_of_the_process
from merge_sort import merge_sort


from random import sample, randint

def hybrid_sort(lst, start=0, end=None):

    start = start or 0
    end = end or len(lst)-1

    if end - start < 36:
        insertion_sort(lst, start, end)

    else:
        pivot = randint(start, end)

        if pivot!= end:
            lst[pivot], lst[end] = lst[end], lst[pivot]
        pivot = lst[end]

        cur, gr, leq = start, start, start
        while cur <= end-1:
            if lst[cur] <= pivot:
                lst[cur], lst[gr] = lst[gr], lst[cur]
                gr += 1
            cur += 1

        lst[gr], lst[end] = lst[end], lst[gr]

        hybrid_sort(lst, leq, gr-1)
        hybrid_sort(lst, gr+1, end)

    return lst


def test():
    def case(lst):
        result = hybrid_sort(lst)
        print 'Ok'

    case([])
    case([1])
    case([1, 3, 2])
    case([1, 5, 5, 7])
    case([4, 3, 2, 1])
    case(sample(xrange(1000), 5))
    case(sample(xrange(1000), 15))
    case(sample(xrange(1000), 41))
    case(sample(xrange(1000), 100))
    case(sample(xrange(1000000000), 100000))


if __name__ == '__main__':
    lst = sample(xrange(1000000000), 100000)

    print 'Time_QS', time_of_the_process(lst, quick_sort)
    print 'Time_HS', time_of_the_process(lst, hybrid_sort)
    print 'Time_MS', time_of_the_process(lst, merge_sort)
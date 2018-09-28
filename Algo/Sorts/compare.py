#! usr/bin/env python2.7
# coding: utf-8

from insertion_sort import insertion_sort
from quick_sort import quick_sort
from expected_bound import time_of_the_process
from merge_sort import merge_sort
from hybrid_sort import hybrid_sort

from random import sample, randint

def main(n):
    expectation_QS = 0
    expectation_HS = 0
    #expectation_MS = 0

    for i in range(n):
        lst = sample(xrange(1000000000), 100000)
        expectation_QS += time_of_the_process(lst, quick_sort)
        expectation_HS += time_of_the_process(lst, hybrid_sort)
        #expectation_MS += time_of_the_process(lst, merge_sort)

    print 'Expected Time of processes with arrays cardinality 100000'
    print 'Time_QS :', expectation_QS/n
    print 'Time_HS :', expectation_HS/n 
    #print 'Time_MS :', expectation_MS/n



if __name__ == '__main__':
    main(100)
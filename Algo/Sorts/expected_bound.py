#! usr/bin/env python2.7
# coding: utf-8

from insertion_sort import insertion_sort
from quick_sort import quick_sort

from collections import defaultdict
from copy import copy
from random import sample
from timeit import default_timer


def time_of_the_process(lst, func):
	start = default_timer()
	func(lst)
	time = default_timer() - start

	return time

def time_comparison(lst, sort1, sort2):
	dif = time_of_the_process(copy(lst), sort1) - time_of_the_process(copy(lst), sort2)
	return dif

def bound_search(cnt):
	while time_comparison(sample(xrange(1000000), cnt), insertion_sort, quick_sort) < 0:
		cnt += 1

	return cnt

def counting_expectation(n):
	dict_of_repetition = defaultdict(lambda : 0)
	for i in xrange(n):
		dict_of_repetition[bound_search(7)] += 1

	expectation = 0
	for key in dict_of_repetition:
		expectation += (key * 1.0 * dict_of_repetition[key]/n)

	print expectation


if __name__ == '__main__':
	counting_expectation(1000)
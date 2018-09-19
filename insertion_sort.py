#! usr/bin/env python2.7
# coding: utf-8

from random import sample

def insertion_sort(lst, start=0, end=None):

	start = start or 0
	end = end or len(lst)

	for i in range(start+1, end):
		key = lst[i]
		j = i-1

		while j >= start and lst[j] > key:
			lst[j+1], lst[j] = lst[j], lst[j+1]
			j -= 1

		lst[j+1] = key

	return lst


def test():
	def case(lst):
		result = insertion_sort(lst)
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


if __name__ == '__main__':
	test()
	print 'Well played'
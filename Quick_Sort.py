#! usr/bin/env python2.7
# coding: utf-8

from random import randint, sample

def quick_sort(lst, start=0, end=None):

	end = end or len(lst)-1

	if len(lst) > 1 and start < end:

		p = randint(start, end)

		if p!= end:
			lst[p], lst[end] = lst[end], lst[p]
		pivot = lst[end]

		i, j, l = start, start, start
		while i <= end-1:
			if lst[i] <= pivot:
				lst[i], lst[j] = lst[j], lst[i]
				j += 1
			i += 1

		lst[j], lst[end] = lst[end], lst[j]

		quick_sort(lst, start, j-1)
		quick_sort(lst, j+1, end)

	return lst


def test():
	def case(lst):
		result = quick_sort(lst)
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
	test()
	print "Well played"
#! usr/bin/env python2.7
# coding: utf-8

from random import randint, sample

def quick_sort(lst, start=0, end=None):

	end = end or len(lst)-1

	if len(lst) > 1 and start < end:

		pivot = randint(start, end)

		if pivot != end:
			lst[pivot], lst[end] = lst[end], lst[pivot]
		pivot = lst[end]

		cur, gr, leq = start, start, start
		while cur <= end-1:
			if lst[cur] <= pivot:
				lst[cur], lst[gr] = lst[gr], lst[cur]
				gr += 1
			cur += 1

		lst[gr], lst[end] = lst[end], lst[gr]

		quick_sort(lst, leq, gr-1)
		quick_sort(lst, gr+1, end)


	return lst


def test():
	def case(lst):
		result = quick_sort(lst)
		print result, 'Ok'

	case([])
	case([1])
	case([1, 3, 2])
	case([1, 5, 5, 7])
	case([4, 3, 2, 1])
	case(sample(xrange(1000), 5))
	case(sample(xrange(1000), 15))
	case(sample(xrange(1000), 41))
	case(sample(xrange(1000), 100))
	#case(sample(xrange(1000000000), 100000))


if __name__ == '__main__':
	test()
	print "Well played"
#! usr/bin/env python2.7
# coding: utf-8

from random import randint, sample

#def order(lst):
#    if lst[0].isalpha() == True:
#    def __lt__(self, other):
#        return chr(min(ord(self), ord(other)))

def merge_sort(lst):
    if len(lst) < 2:
        return lst
    mid = len(lst)/ 2
    return merge(merge_sort(lst[:mid]), merge_sort(lst[mid:]))


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result



def test():
	def case(lst):
		result = merge_sort(lst)
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

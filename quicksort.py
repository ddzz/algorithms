# Python quicksort implementation
# O(nlog(n)) running time
# This implementation uses the first element of each subarray as the pivot element

counter = 0

def quicksort(array,start,end):
	global counter
	
	if start >= end:

		return 0
		
	else:
		part = partition(array,start,end)
		left = quicksort(array,start,part)				
		right = quicksort(array,part+1,end)
		return counter


def partition(array,l,r):
	global counter
	counter += r-l-1

	p = array[l]
	
	i = l + 1

	for j in range(l+1,r):
		if array[j] < p:					
			array[i], array[j] = array[j], array[i]
			i += 1			

	array[l], array[i-1] = array[i-1], array[l]
	return i-1

array = []
for line in open('qs.txt','r').readlines():	
	array.append(int(line))

print quicksort(array,0,len(array))

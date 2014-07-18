array = []
for line in open('qs.txt','r').readlines():	
	array.append(int(line))

def quicksort(array,start,end) :
	counter = 0
	
	if start >= end:

		return 0
		
	else:
		part = partition(array,start,end)
		counter = end - start
		counter -= 1
		left = quicksort(array,start,part)				
		right = quicksort(array,part+1,end)
		return counter + left + right


def partition(array,l,r):

	array[l], array[r-1] = array[r-1], array[l]
	p = array[l]
	
	i = l + 1

	for j in range(l+1, r):
		if array[j] <= p:					
			array[i], array[j] = array[j], array[i]
			i += 1			

	array[l], array[i-1] = array[i-1], array[l]
	return i-1



print len(array)
print quicksort(array,0,len(array))
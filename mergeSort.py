# Recursive merge sort algorithm
# O(nlogn) running time


def mergeSort(array):

	if len(array) <= 1:
		pass
		
	else:
		mid = len(array)//2
		left = array[:mid]
		right = array[mid:]
		
		mergeSort(left)
		mergeSort(right)
		
		i = 0
		j = 0
		k = 0
		for k in range(len(array)):
			if len(left) > i and len(right) > j:
				if left[i] < right[j]:
					array[k] = left[i]
					i += 1
				else:
					array[k] = right[j]
					j += 1
			else:
				if len(left) > i:
					array[k] = left[i]
					i += 1
				if len(right) > j:
					array[k] = right[j]
					j += 1
	return array	
	
array = [ ]
for line in open("IntegerArray.txt",'r').readlines():	
	array.append(int(line))
newarray = mergeSort(array)

print newarray
		

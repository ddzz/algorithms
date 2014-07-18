# This algorithm calculates the sum of the rolling median of a
# stream of integers using a min heap and max heap to reduce
# the running of the algorithm.

from heapq import heappush, heappop

arrayleft = []
arrayright = []

total = 0

array = []

for line in open('Median.txt', 'r').readlines():
	    array.append(int(line))

for i in array:
    if len(arrayleft) == 0:
        heappush(arrayleft, -i)
    else:
        if i > -arrayleft[0]:
            heappush(arrayright, i)
        else:
            heappush(arrayleft, -i)

    if len(arrayleft) - len(arrayright) >= 2:
        heappush(arrayright, abs(heappop(arrayleft)))
    elif len(arrayright) > len(arrayleft):
        heappush(arrayleft, -heappop(arrayright))

    total += abs(arrayleft[0])

print total
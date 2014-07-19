# Recursive binary search algorithm

def binarySearch(array, key):
    if len(array) == 1 and array[0] != key:
        print "Search key not found in array"

    else:
        midpt = len(array)//2

        if array[midpt] > key:
            binarySearch(array[:midpt], key)
        elif array[midpt] < key:
            binarySearch(array[midpt:], key)
        else:
            print "Key has been found"


binarySearch(array, key)

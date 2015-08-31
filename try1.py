def modifyArray(array):
    print id(array)
    for i in xrange(0, len(array)):
        array[i] += 1
array = [0 for i in xrange(0, 10)]
subArray1 = array[0:5]
modifyArray(subArray1)
subArray2 = array[0:5]
modifyArray(subArray2)
modifyArray(array)
print array
array = [1,2,3]
print array[::-1]
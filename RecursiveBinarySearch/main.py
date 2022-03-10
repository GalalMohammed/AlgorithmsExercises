def BinarySearch (arr, firstIndex, lastIndex, num):
    if firstIndex < lastIndex and arr[(firstIndex + lastIndex) // 2] != num:
        if arr[(firstIndex + lastIndex) // 2] < num:
            return BinarySearch(arr, ((firstIndex + lastIndex) // 2) + 1, lastIndex, num)
        else:
            return BinarySearch(arr, firstIndex, ((firstIndex + lastIndex) // 2) - 1, num)
    else:
        if arr[(firstIndex + lastIndex) // 2] == num:
            return (firstIndex + lastIndex) // 2
        else:
            return -1
print(BinarySearch([1, 3, 4, 5, 7], 0, 4, 1))

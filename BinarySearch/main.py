def BinarySearch (arr, firstIndex, lastIndex, num):
    while arr[(firstIndex + lastIndex) // 2] != num:
        if firstIndex < lastIndex:
            if arr[(firstIndex + lastIndex) // 2] < num:
                firstIndex = ((firstIndex + lastIndex) // 2) + 1
            else:
                lastIndex = ((firstIndex + lastIndex) // 2) - 1
        else:
            return -1
    return (firstIndex + lastIndex) // 2
print(BinarySearch([1, 3, 3, 4, 7], 0, 4, 8))

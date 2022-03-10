def SelectionSort (arr, length):
    new_arr = []
    for i in range(length):
        smallest = arr[0]
        for j in range(1, length - i):
            if arr[j] < smallest:
                smallest = arr[j]
        new_arr.append(arr.pop(arr.index(smallest)))
    return new_arr
print(SelectionSort([5, 3, 3, 2, 10], 5))

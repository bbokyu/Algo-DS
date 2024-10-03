

arr = [3,2,1,6,7,8,5,10,4, 9, 0, 69]


# Merge Sort
def merge_sort(arr):
    # Base Case
    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    # split
    left = merge_sort(arr[0:middle])
    right = merge_sort(arr[middle:])

    merged = merge(left, right)

    return merged

def merge(left, right) -> any:
    merged_arr = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
    
    mergedArr += left[i:] or right[j:]

    return mergedArr

# print(mergeSort(arr))

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    # we say pivot is just last element of arr
    pivot = arr[-1]

    left = []
    right = []

    for n in arr[:-1]:
        if n <= pivot:
            left.append(n)
        else:
            right.append(n)
    
    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    return sorted_left + [pivot] + sorted_right

print(quick_sort(arr))


#
#
# arr = [3,2,1,6,7,8,5,10,4, 9, 0, 69]
#
#
# # Merge Sort
# def mergeSort(arr):
#
#     # Base Case
#     if len(arr) <= 1:
#         return arr
#
#     middle = len(arr) // 2
#
#     # split
#     left = mergeSort(arr[0:middle])
#     right = mergeSort(arr[middle:])
#
#     merged = merge(left, right)
#
#     return merged
#
# def merge(left, right):
#
#     mergedArr = []
#
#     i = 0
#     j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             mergedArr.append(left[i])
#             i += 1
#         else:
#             mergedArr.append(right[j])
#             j += 1
#
#     mergedArr += left[i:] or right[j:]
#
#     return mergedArr
#
# # print(mergeSort(arr))
#
#
# def quickSort(arr):
#
#     if len(arr) <= 1:
#         return arr
#
#     # we say pivot is just last element of arr
#     pivot = arr[-1]
#
#     left = []
#     right = []
#
#     for n in arr[:-1]:
#         if n <= pivot:
#             left.append(n)
#         else:
#             right.append(n)
#
#     sortedLeft = quickSort(left)
#     sortedRight = quickSort(right)
#
#     return sortedLeft + [pivot] + sortedRight
#
# print(quickSort(arr))
#

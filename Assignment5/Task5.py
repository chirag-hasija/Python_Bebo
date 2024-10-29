# lis = [3,6,8,10,1,2,1]
# lis.sort(reverse= True)
# print(lis)
# def quick_sort(arr):
#     # Base case: if the array has 1 or 0 elements, it's already sorted
#     if len(arr) <= 1:
#         return arr
#     else:
#         # Select a pivot element
#         pivot = arr[len(arr) // 2]
#
#         # Partition the array into three parts: less, equal, and greater
#         less = [x for x in arr if x < pivot]
#         print(less)
#         equal = [x for x in arr if x == pivot]
#         print(equal)
#         greater = [x for x in arr if x > pivot]
#         print(greater)
#
#         # Recursively apply quicksort to 'less' and 'greater' sub-arrays and combine the results
#         return quick_sort(less) + equal + quick_sort(greater)

def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)


def partition(arr, low, high):
    p = arr[low]
    i = low + 1
    j = high

    while True:
        while i <= j and arr[i] <= p:
            i += 1
        while i <= j and arr[j] >= p:
            j -= 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[low], arr[j] = arr[j], arr[low]
    return j


# Example usage
arr = [10, 7, 8, 9, 1, 5]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


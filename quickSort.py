def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it is already sorted
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (Here, we choose the last element as the pivot)
    pivot = arr[len(arr) - 1]
    left = []   # Elements less than the pivot
    right = []  # Elements greater than the pivot
    equal = []  # Elements equal to the pivot

    # Partition the array into left (smaller), equal, and right (larger)
    for num in arr:
        if num < pivot:
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            equal.append(num)

    # Recursively apply quick sort to left and right parts
    return quick_sort(left) + equal + quick_sort(right)

# Example usage:
arr = [10, 7, 8, 9, 1, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)

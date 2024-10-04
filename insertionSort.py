def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Current element to be positioned
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than 'key'
        # one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key after the element just smaller than it
        arr[j + 1] = key

    return arr

# Example usage:
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)

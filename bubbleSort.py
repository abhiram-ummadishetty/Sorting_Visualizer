def bubblesort(arr,n):
    swapped = False
    for i in range(n):
        for j in range(1,n-i):
            if arr[j]<arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                swapped = True
        if not swapped:
            return arr
    return arr


# n = int(input("Enter number of elements: "))
array = [2,5,7,1,3,9,8]
n = len(array)
print(bubblesort(array,n))

    
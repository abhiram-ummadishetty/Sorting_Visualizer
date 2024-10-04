def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left,right)

def merge(left,right):
    sorted_array =[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_array.append(left[i])
            i+=1
        else:
            sorted_array.append(right[j])
            j+=1
    while i<len(left):
        sorted_array.append(left[i])
        i+=1
    while j<len(right):
        sorted_array.append(right[j])
        j+=1

    return sorted_array

array = [4,2,11,1,2,2,3]
print(mergesort(array))
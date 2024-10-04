def selectionsort(arr,n):
    for i in range(n):
        min_idx = i
        j = i
        while(j!=n):
            if arr[j]<arr[min_idx]:
                min_idx = j
            j+=1
        if min_idx!=i:
            arr[i],arr[min_idx]= arr[min_idx],arr[i]
    return arr

array = [2,5,7,1,3,9,8]
n = len(array)
print(selectionsort(array,n))

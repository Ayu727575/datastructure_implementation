def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j = i-1
        while j>=0 and arr[j]>temp:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = temp

arr = [30,23,28,30,11,14,19,16,21,25]
insertion_sort(arr)
print(arr)
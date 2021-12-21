arr = [0,17,14,15,11,2,4,16,5,6,3]

for i in range(len(arr)//2+1):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
print(sorted(arr))
print(arr[len(arr)//2])


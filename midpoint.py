arr = [0,1,2,4,5,6,3]

for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print(arr[len(arr)//2])


# i = 3
# j = 6

# arr[i] = 4
# arr[j] = 3

# 0 1 2 3 5 6 4


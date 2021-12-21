arr = [
    [11,2,4],
    [4,5,6],
    [10,8,-12]
]

l,r = 0,0

for i in range(len(arr)):
    l += arr[i][i]
    r += arr[i][-i-1]

print(abs(l-r))

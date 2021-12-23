arr = [
    [112,42,83,119],
    [56,125,56,49],
    [15,78,101,43],
    [62,98,114,108]
]

mid = len(arr) //2
top, bottom = 0, 0
first = 0

# for a in arr:
#     for i in range(mid):
#         first += a[i]

for i in range(mid):
    for j in range(mid):
        top += arr[i][j]
        print(top)



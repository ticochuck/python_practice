x, y, z = 1, 2, 1
n = 3

list_3d = []

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            list_3d.append([i,j,k])
    
for arr in list_3d:
    if sum(arr) != n:
        print(arr, end=" ")
print('\n',list_3d)




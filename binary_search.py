# arr = [0,1,2,3,4,5,6,7,8,9,10]

arr =[-1,0,3,5,9,12]
# arr = [-1, 0,1,2,3,4,5,6,7,8,9,10,50,60,70,80,90,100,115,200, 201, 202,203,348,420,422,423,424,425,430,444,560,590,750,888,900,901,902,903,904,1000]
val = int(input('Please enter a value: '))

def binary_search(arr, val):

    start = 0
    end = len(arr) -1 
    
    if arr[0] == val:
        print(f'We found the value in position in index 0')
        return 0
    elif arr[end] == val:
        print(f'We found the value in position in last index')
        return end

    while start <= end:

        mid = (start + end) // 2
        if arr[mid] == val:
            print(f'We found the value in position {mid}')
            return mid
        elif arr[mid] > val:
            end = mid - 1
        else:
            start = mid + 1
            
    print(f'{val} is not in the array.')
    return -1

binary_search(arr, val)
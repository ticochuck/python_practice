arr = [0,1,2,3,4,5,6,7,8,9,10,50,60,70,80,90,100,115,200,348,420,444,560,590,750,888,900,901,902,903,904,1000]

val = int(input('Please enter a value: '))
print(f'searching for {val} in the array')4

mid = arr[len(arr)//2]

def binary_search(arr, val, mid):

    if val == mid:
        return print(f"Found the {val} in the array")
    elif val <= mid:
        arr = arr[:mid]
        return binary_search(arr, val, mid)
    else:
        arr = arr[mid:]
        return binary_search(arr, val, mid)

    
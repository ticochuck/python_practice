# Function to find if there are distinc indices where arr[i] == arr[j] and abs(i-j) <= k

nums = [1,0,1,2]
k = 1
def containsNearbyDuplicate(nums, k):
        
    temp = {}
    count = 0 
    
    for num in nums:
        count += 1
        if num in temp:
            temp[num].append(count-1)
            print(temp[num])
            if abs(temp[num][0]-temp[num][1]) <= k:
                return True
            else:
                temp[num].remove(temp[num][0])
        else:
            temp[num] = [count-1]
    
    return False

print(containsNearbyDuplicate(nums, k))
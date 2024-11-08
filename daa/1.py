def binary_search(low,high,target,arr):
    
    if low<=high:
        
        mid = (low+high)// 2
       
        if arr[mid] == target:
        
            return mid
        elif arr[mid]>target:
            high = mid-1
            return binary_search(low,high,target,arr)
        else:
            low = mid+1
            return binary_search(low,high,target,arr)
    else:
        return -1

arr = [2,5,3,1]
target = 3
arr.sort()
ans = binary_search(0,len(arr)-1,target,arr)
if ans!=-1:
    print("ans:",ans)
else:
    print("no")
    


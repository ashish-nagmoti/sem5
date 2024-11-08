#divide and conquer and nlogn
class quickSort:
    def partition(self,low,high,arr):
        pivot = arr[high]
        i = low-1
        for j in range(low,high):
            if arr[j] <pivot:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    
    def quick_sort(self,low,high,arr):
        if low<high:
            index = self.partition(low,high,arr)
            self.quick_sort(low,index-1,arr)
            self.quick_sort(index+1,high,arr)

    def quick(self,arr):
        self.quick_sort(0,len(arr)-1,arr)

unsorted_arr = input("enter array")
unsorted_arr = list(map(int,unsorted_arr.split()))
sorter = quickSort()
sorter.quick(unsorted_arr)
print(unsorted_arr)

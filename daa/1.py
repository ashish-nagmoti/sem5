def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    steps = 0

    while low <= high:
        mid = (low + high) // 2
        steps += 1

        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1, steps


arr = input("enter array separeted by spaces")
arr = list(map(int,arr.split()))
target = int(input("enter target"))
index, steps = binary_search(arr, target)

if index != -1:
    print(f"Target {target} found at index {index} in {steps} steps.")
else:
    print(f"Target {target} not found in the array in {steps} steps.")


''' implement the binary search algorithm '''

arr = [int(val) for val in input("Enter elements of array (comma seperated) ").split(",")]

sval = int(input("Enter element to be found "))

arr.sort()                                                          # elements are required to be sorted for binary search
low = 0
high = len(arr)-1


while low <= high:
    mid = (low+high)//2
    if sval > arr[mid]:                                             # element is toward right side
        low = mid+1
    elif sval < arr[mid]:                                           # element is toward left side
        high = mid-1
    elif sval == arr[mid]:
        print(f"Search element found at {mid} index in array")
        break
else:
    print("Element not found in array")
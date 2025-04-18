''' implement the linear search algorithm '''

arr = [int(val) for val in input("Enter elements of array (comma seperated) ").split(",")]

sval = int(input("Enter element to be found "))

for i in range(len(arr)):
    if arr[i] == sval:
        print(f"Search element exists at {i} index in array")
        exit()
else:
    print("Element not found")


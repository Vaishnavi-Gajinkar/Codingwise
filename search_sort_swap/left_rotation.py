''' implement left roation in an array for n times '''

arr = [int(val) for val in input("Enter elements of array (comma seperated) ").split(",")]
n = int(input("How many times do you want to rotate left? "))

# --- way 1 -----
for iter in range(1,n+1):
    t = arr[0]
    moves = 0
    while moves < len(arr)-1:
        arr[moves] = arr[moves+1]
        moves += 1
    arr[len(arr)-1] = t
    print(f'Result after rotating {iter} times:',arr)

# --- way 2 -----
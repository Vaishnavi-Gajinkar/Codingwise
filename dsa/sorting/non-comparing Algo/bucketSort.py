''' wap to implement the Bucket sort algorithm in dsa '''
''' when array elements are in decimal, multiply them with multiples of 10 such that there's only one digit before decimal.
    create 10 sub-arr in a main arr and add the number in a bucket corresponding to respective result '''

# import math

def bucketSort(arr:list):
    new_arr = [[]]*10

    for val in range(len(arr)):
        buk = int(arr[val]*10)
        new_arr[buk].append(arr[val])
    
    for i in range(len(new_arr)):
        for j in range(len(new_arr[i])):
            print(new_arr[i][j])


x = [0.1,0.2,0.3,0.4,0.5,0.6]
# x = [0.34,0.66,0.13,0.87,0.97,0.23,0.34,0.13,0.95,0.38,0.17,0.91]
bucketSort(x)

# verify solution
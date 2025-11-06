''' wap to implement the Bucket sort algorithm in dsa '''
''' when array elements are in decimal, multiply them with multiples of 10 such that there's only one digit before decimal.
    create 10 sub-arr in a main arr and add the number in a bucket corresponding to respective result '''

# import math

def bucketSort(arr:list):
    new_arr = [[] for i in range(10)]

    for val in range(len(arr)):
        buk = int(arr[val]*10)
        new_arr[buk].append(arr[val])
    
    for i in range(len(new_arr)):
        for j in range(len(new_arr[i])):
            print(new_arr[i][j], end=", ")


x = [0.34,0.66,0.13,0.87,0.97,0.23,0.34,0.13,0.95,0.38,0.17,0.91]
bucketSort(x)


'''
OUTPUT:
0.13, 0.13, 0.17, 0.23, 0.34, 0.34, 0.38, 0.66, 0.87, 0.97, 0.95, 0.91, 
'''
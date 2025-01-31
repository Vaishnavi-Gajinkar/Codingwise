""" Write a while loop to print the Fibonacci series upto 10 terms """
""" 1+2+3+4+5+6+7+8+9+10"""

num = 10
sum = 0
i = 1
print(f'Fibonacci series uptil {num} is as below ')
while i in range(1,num+1):
    if i < num:
        print(i,end="+")
    else:
        print(i,end="=")
    sum += num
    i += 1
print(sum)


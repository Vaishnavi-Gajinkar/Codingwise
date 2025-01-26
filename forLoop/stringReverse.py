""" Use a for loop to reverse a string (eg. 'hello' to 'olleh')"""

str1 = 'hello'
for ch in range(-1,-(len(str1)+1),-1):
    print(str1[ch], end='')

str2 = input("Enter your string: ")
for strt in range(len(str2)):
    for end in range(len(str2)):
        fhaf = str2[strt]
        shaf = str2[-end]
        strev = shaf + fhaf
        print(strev)
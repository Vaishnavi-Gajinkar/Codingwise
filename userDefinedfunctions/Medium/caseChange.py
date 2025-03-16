'''convert the case of inputed string (lower if upper and vice versa)'''

class CaseConverter:

    def fun(self, string):
        
        lst = []

        for ch in string:
            if ord(ch) >= 65 and ord(ch) <= 90:
                diff = ord(ch)-ord('A')
                find = ord('a')+diff
                lst.append(chr(find))
            
            elif ord(ch) >= 97 and ord(ch) <= 122:
                diff = ord(ch)-ord('a')
                find = ord('A')+diff
                lst.append(chr(find))

        return lst
    
inp = input("Enter a string with mixed case of characters ")
obj = CaseConverter()
res = ''.join(obj.fun(inp))
print("Result after reversing case of each character is",res)
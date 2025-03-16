'''find the length of a string'''

class Calc:
    counter = 0

    def method(self, word):
        for ch in word:
            self.counter += 1
        return self.counter
    
accept = input("Enter a string input ")

obj = Calc()
res = obj.method(accept)

print(f'Your entered string is {res} characters long')

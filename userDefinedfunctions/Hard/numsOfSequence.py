'''print the first n numbers of a sequence defined as (n+1)*(n-1)'''

class seq:
    def __init__(self,num):
        self.num = num

    def addi(self):
        return self.num+1
    def subs(self):
        return self.num-1
    def mult(self):
        return self.addi*self.subs
    
end = int(input("Enter the end number of sequence "))
res = []
for n in range(1,end+1):
    obj1 = seq(n)
    obj2 = seq(n)
    prod = seq.mult()
    res.append(prod)
print(res)

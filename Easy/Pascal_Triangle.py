class Solution:
    def solve(self,n):
        if n == 0:
            return [1]
        if n == 1:
            return [1,1]
        fs = [1,1]
        temp = [1,1]
        for i in range(2,n+1): # first loop
            fs = temp
            temp = [1]
            for i in range(len(fs)-1): #second loop to create the numbers within [1, x ,1]
                temp.append(fs[i]+fs[i+1])
            temp.append(1)
        return temp
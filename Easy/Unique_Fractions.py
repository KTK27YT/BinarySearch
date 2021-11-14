from math import gcd
class Solution:
    def solve(self,fractions):
        res = set()
        for x , y in fractions:
            z = gcd(x,y) #Find the GCD of the fraction
            n = x // z  #N representing Numerator, divide the Numerator by GCD
            d = y // z  #D representing Denominator , divide the Denominator by GCD
            res.add((n,d))  #add the newly simplified fraction to another list
            return sorted(res, key=lambda x: x[0] / x[1]) #return the list by sorting it from smallest to largest
from sys import stdin, stdout
#from fractions import Fraction

class Fraction: #I decided to make a class fraction since python's default class would not let me define a fraction with a 0 denominator and I needed to assign that value to R in order to perform the binary search
    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)
    
    def __add__(self,otherfraction): #Since the problem uses addition of numerators and denominators i Implemented the addition in the class to do the same and not the normal fraction addition
        newnumerator = self.numerator + otherfraction.numerator
        newdenominator = self.denominator + otherfraction.denominator
        
        return Fraction(newnumerator,newdenominator)
        
    
    def compare(self, otherfraction): #Comparation which returns true if the first given fraction is greater than the other and false if not
        b = Fraction(self.numerator*otherfraction.denominator,self.denominator*otherfraction.denominator) #To avoid using greatest common divisor I multiply each fraction by the denominator of the other one
        c = Fraction(otherfraction.numerator*self.denominator,otherfraction.denominator*self.denominator) #Like this I can have the same denominators to make the comparison
        if (int(b.numerator) > int(c.numerator)):return True #Since they have the same denominator I compare the numerators in order to determine whether the first fraction is greater or not
        else:return False


def solve(m,n): 
    L, R, k = Fraction(0,1), Fraction(1,0), Fraction(m,n) #We know that the first level of the tree is L 0/1 R1/0 and the given fraction which is k
    while (True): #At each node, k will either be in the left half of the tree, or the right half. So we use binary search to find it
        M = L+R #insert m+m'/n+n' between two adjacent fractions m/n and m'/n' as it says in the problem
        if (Fraction.compare(k,M)): #If k is greater than M then we know that we must take the right path in order to find k, and then verify the following node
            L = Fraction(M.numerator, M.denominator)
            stdout.write('R')
        elif (Fraction.compare(M,k)): #If k is smaller than M then we know that we must take the left path in order to find k, and then verify the following node
            R = Fraction(M.numerator, M.denominator)
            stdout.write('L')
        else: break #If k = M then we know we have found our k and we have already printed the path
    
def main():
    inp = stdin
    tok = stdin.readline().strip().split() #Read the line from std input
    m,n = int(tok[0]),int(tok[1]) #Since values are split into an array I take the first position as m and the second as n
    while (m*n!=1):
        (solve(m,n))
        print ()
        tok = stdin.readline().strip().split() #Assign new values to m,n in order to avoid an infinite loop
        m,n = int(tok[0]),int(tok[1])
    
main()

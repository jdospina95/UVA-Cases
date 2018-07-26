from sys import stdin

def pal(A,i,j):
    ans=True
    while ans and i < j:
        ans,i,j = A[i] == A[j-1],i+1,j-1 #Check whether the string is a palindrome or not, return ans = True if it is and ans = False if not
    return ans

def phi_tab(A):
    
    
#     Input: A[0..N), N>=0
#     Output: minimum quantity of palindrome substrings in which A[0..N) can be partitioned
    
    
#     0<= n<=N
    
#     phi(n): minimum quantity of palindrome substrings in which A[0..N) can be partitioned
    
#     pal(i,j) = A[i...j) then it is palindrome
    
    
#     phi(n){ 0		, n=0
    
#     	    1		, n=1
	
# 	min(k|0<=k<=n & pal(k,n) : 1+ phi(k)) , n!=0
    
    
    
    N=len(A)
    tab,n = [float('inf') for i in range(N+1)],1
    tab[0]=0
    while n!=N+1:
        for k in range(n):
            if pal(A,k,n):
                tab[n] = min(tab[n], 1+tab[k])
        n +=1
    return tab[N]

def main():
    inp = stdin
    cases = int(inp.readline())
    while cases!=0:
        print(phi_tab(inp.readline().strip()))
        cases -=1
        
main()

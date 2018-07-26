from sys import stdin

MAX = 101
coins = [ None for i in range(MAX) ]

def phi_tab(B,W,M): #Optimal knapsack seen in class with it's O(N) spatial complexity
  #   B:  Benefit
  #   W:  Weight
  #   M:  Max Weight
  tab,N = [ 0 for m in range(M+1) ],len(B)
  n,m = 1,M
  # Invariants: P0, P1, P2, P3
  #   P0 : (A j | 0 <= j <= m : tab[j] = phi(n-1,j))
  #   P1 : (A j | m < j <= M : tab[j] = phi(n,j))
  #   P2 : 0 <= n <= N+1
  #   P3 : -1 <= m <= M
  while n!=N+1:
    if m==-1: n,m = n+1,M
    else:
      if W[n-1]<=m: tab[m] = max(tab[m],B[n-1]+tab[m-W[n-1]])
      m -= 1
  return tab[M]
    
def solve(m):
    global coins
    maxweight = 0 # Since we are using the knapsack in a different way we need to establish the maxweight the knapsack can carry by adding all the coin values and then diving by 2
    
    for i in range(m):
        maxweight += coins[i]
    
    maxweight2 = int(maxweight >> 1)
    
    if (maxweight%2 == 0): return ((maxweight2 - phi_tab(coins[0:m], coins[0:m], maxweight2))*2) # Since sometimes the division of maxweight is not exact we need two return types, normal one for when the division is exact
    else: return (((maxweight2 - phi_tab(coins[0:m], coins[0:m], maxweight2))*2) + 1) # and adding a 1 to the return for it to work correctly

def main():
  global coins
  inp = stdin
  cases = int(inp.readline().strip()) #cases contains the number of cases for the problem
  while cases>0:
    m = int(inp.readline().strip()) #n contains the number of coins
    if (m==0): # This is used as something like a try catch because when we have 0 coins the next stdin line will be empty and this would cause an error when trying to fill the coins list
        x = inp.readline()
        print(0)
    else:
        tok = inp.readline().strip().split()
        for i in range(m): coins[i] = int(tok[i]) #store all the carriages into an array called train
        print(solve(m))
    cases -= 1

main()

from sys import stdin

MAX = 610
sites = [ None for i in range(MAX) ]
sums,omin,omax,n,k = None,None,None,None,None

def solve():
  global sites,sums,omin,omax,n,k
  sites2 = sites[0:n] # from 0:n to avoid comparing the None type values, like this I ignore them
  first = 0
  sums2 = sums # aux copy of sums in order to change the stored value since sums is a global variable
  
  while (first + 1 != sums2): # sums2 is used in this modified binary search as the higher value
    midpoint = first + ((sums2 - first) >> 1)
    if (midpoint < omax):
      first = midpoint
    else:
      i = 0
      midpoint2 = midpoint # auxiliar copy of midpoint to change value according to some conditions
      k2 = k # auxiliar copy of number of nights to change value according to some conditions
      aux = 0 # auxiliar variable to store the value of the midpoint in sums2 in case the first two conditions are not satisfied
      while (i < len(sites2)):
        if (midpoint2 >= sites2[i]):
          midpoint2 -= sites2[i] # assume this distance has been traveled already in the day
        elif (midpoint >= sites2[i] and k2 > 0):
          midpoint2 = midpoint - sites2[i] # assumes that the day is already over and this was the distance traveled
          k2 -= 1
        else:
          aux = -1 # none of the above conditions were satisfied and sums != midpoint, set the lower bound of the binary search to the midpoint to continue iterating
        i += 1
      if (aux == 0):
        sums2 = midpoint
      else:
        first = midpoint
  
  return sums2

def main():
  global sites,sums,omin,omax,n,k
  inp = stdin
  l = stdin.readline().strip()
  while len(l)>0:
    n,k = [ int(x) for x in l.split() ]
    n += 1
    omin,omax,sums = float('inf'),float('-inf'),0
    for i in range(n):
      sites[i] = int(inp.readline().strip())
      if sites[i]>omax: omax = sites[i]
      if sites[i]<omin: omin = sites[i]
      sums += sites[i]
    if sums==0:
      print(0)
    else:
      print(solve())
    l = stdin.readline().strip()

main()

from sys import stdin

marble,lenm = None,None

def solve(x):
  global marble,lenm
  first = 0
  last = len(marble)-1
  found = False
  while (first<=last):
    midpoint = first + ((last - first) >> 1)
    if marble[midpoint] == x:
      respuesta = midpoint #when found I store into the variable respuesta the position where it was found so that I can return through a binary search the position of the element
      found = True
      last = midpoint-1
    else:
      if x < marble[midpoint]:
        last = midpoint-1
      else:
        first = midpoint+1
  
  if (found):
    return respuesta
  else:
    return -1

def main():
  global marble,lenm
  inp = stdin
  cas = 1
  lenm,lenq = [ int(x) for x in inp.readline().split() ]
  while lenm+lenq!=0:
    marble = [ int(inp.readline()) for i in range(lenm) ]
    marble.sort()
    print('CASE# {0}:'.format(cas))
    for q in range(lenq):
      x = int(inp.readline())
      ans = solve(x)
      if ans==-1 or marble[ans]!=x:
        print('{0} not found'.format(x))
      else:
        print('{0} found at {1}'.format(x,ans+1))
    lenm,lenq = [ int(x) for x in inp.readline().split() ]
    cas += 1

main()

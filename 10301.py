from sys import stdin

def intersect(a,b):
  global rings
  diff = ((rings[a][0] - rings[b][0])**2) + ((rings[a][1] - rings[b][1])**2)
  return (((rings[a][2] - rings[b][2])**2) <= diff and diff <= ((rings[a][2] + rings[b][2])**2))
  
def joinGroups(a,b):
  global groupsb
  if (a!=b):
    for i in range(len(b)):
      groupsb[b[i]] = a
      a.append(b[i])

def solve():
    ans = 0
    global rings, groupsb, intersection
    for i in range(len(rings)):
      intersection[i] = []
      intersection[i].append(i)
      groupsb[i] = intersection[i]
      
      for j in range(i):
        if intersect(i,j): joinGroups(groupsb[j], groupsb[i])
    
    ans = 0
    for i in range(len(rings)):
      ans = max(ans, len(groupsb[i]))
      
    return ans

def main():
    global rings, groupsb, intersection
    inp = stdin
    n = int(inp.readline().strip())
    while (n!=-1):
        rings = [ None for i in range(n) ]
        groupsb = [ None for i in range(n) ]
        intersection = [ None for i in range(n) ]
        for i in range(n):
            x, y, r = [ float(x) for x in stdin.readline().strip().split() ]
            rings[i] = [x,y,r]
        ans = solve()
        if (ans == 1): print('The largest component contains 1 ring.')
        else: print('The largest component contains {0} rings.'.format(ans))
        n = int(inp.readline().strip())
    
main()

from sys import stdin

class segtree(object):

  def __init__(self,a):
    # Create an empty segment tree
    self.__a = list(a)
    self.__s = [ None for i in range(len(a)<<2) ]
    self.__build_tree(0,0,len(a))

  def __len__(self):
    # Return the length of the collection of values
    return len(self.__a)

  def __str__(self):
    # Return the string representation of the segment tree
    return str(self.__s)
  
  def __left(self,i):
    # Return the index of the left child of i
    return 1+(i<<1)

  def __right(self,i):
    # Return the index of the left child of i
    return (1+i)<<1

  def __build_tree(self,i,low,hi):
    # Store the sum of __a[low..hi) in __s[i]
    ans = None
    if low+1==hi:
      ans = self.__s[i] = self.__a[low]
    else:
      mid = low+((hi-low)>>1)
      ans = self.__s[i] = self.__build_tree(self.__left(i),low,mid) \
                          + self.__build_tree(self.__right(i),mid,hi)
    return ans

  def query_range(self,i,j):
    # Return the sum in the range [i..j)
    assert 0 <= i <= j <= len(self)
    ans = self.__query_aux(0,0,len(self),i,j)
    return ans

  def __query_aux(self,i,low,hi,start,end):
    # Return the sum in the intersection of and  __a[low..hi) and __a[start..end) 
    ans = None
    if hi<=start or end<=low: ans = 0
    elif start<=low and hi<=end: ans = self.__s[i]
    else:
      mid = low+((hi-low)>>1)
      ans = self.__query_aux(self.__left(i),low,mid,start,end) \
            + self.__query_aux(self.__right(i),mid,hi,start,end)
    return ans

  def updateValue(self,i,x):
    # Update the value of the i-th element to be x
    assert 0 <= i < len(self)
    self.__update_aux(0,0,len(self),i,x)

  def __update_aux(self,i,low,hi,j,x):
    assert low<=j<hi
    ans = None
    if low+1==hi: ans = self.__a[j] = self.__s[i] = x
    else:
      mid = low+((hi-low)>>1)
      if j<mid: ans = self.__s[i] = self.__update_aux(self.__left(i),low,mid,j,x) + self.__s[self.__right(i)]
      else: ans = self.__s[i] = self.__s[self.__left(i)] + self.__update_aux(self.__right(i),mid,hi,j,x)
    return ans

def main():
  inp = stdin
  n = int(inp.readline().strip())
  cases = 1
  while (n != 0):
    potmeters = [] #Create a list in order to save all the values for the potentiometers
    for i in range(n):potmeters.append(int(inp.readline().strip())) 
    segmentTree = segtree(potmeters) #Create the segment tree with the potentiometers values
    if (cases > 1): print()
    print ('Case {0}:'.format(cases))
    cases += 1
    text = inp.readline().strip().split()
    while (text[0] != 'END'):
      x, y = int(text[1]), int(text[2])
      if (text[0] == 'M'): #If the given instruction is M then measure the resistance between x and y
        print (segmentTree.query_range(x-1, y))
      elif (text[0] == 'S'): #If the given instruction is S then set potmeter x to y Ohms value
        segmentTree.updateValue(x-1,y)
      text = inp.readline().strip().split()
    n = int(inp.readline().strip())
  
  
main()

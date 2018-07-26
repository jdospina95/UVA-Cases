from sys import stdin

MAX = 25010
train = [ None for i in range(MAX) ]
memo = [ None for i in range(MAX) ]
swaps = 0 
#Created a global variable named "swaps" to store the total amount of position swaps made during the sorting of the list, in order to know 
#how many swaps it takes for the optimal train swapping asuming merge sort is always the optimal one

def merge(A,B):
    global swaps
    sortedlist=[]
    lenA=len(A)
    lenB=len(B)
    i=j=0
    while i<lenA and j<lenB:
        if A[i]<=B[j]:
            sortedlist.append(A[i])
            i=i+1
        else:
            swaps += len(A)-i # len(A) - i is added to the total number of swaps
            sortedlist.append(B[j])
            j=j+1
    if i==lenA:
        sortedlist.extend(B[j:])
    else:
        sortedlist.extend(A[i:])
    return sortedlist

#merge sort implementation from internet with slight modifications
def mergeSort(L):
    N=len(L)
    if N>1:
        firsthalf=mergeSort(L[0:int(N/2)])
        secondhalf=mergeSort(L[int(N/2):])
        return merge(firsthalf,secondhalf)
    else:
        return L

def solve(n):
  global train
  mergeSort(train[0:n]) #since swaps is a golbal variable we just have to call the function merge and it's return is 
                        #not stored into a variable since we don't need the sorted list, it is passed from 0:n since we have the array with some None types which won't be included for sorting
  return swaps

def main():
  global train, swaps
  inp = stdin
  cases = int(inp.readline().strip()) #cases contains the number of cases for the problem
  while cases>0:
    n = int(inp.readline().strip()) #n contains the size of the train
    tok = inp.readline().strip().split()
    for i in range(n): train[i] = int(tok[i]) #store all the carriages into an array called train
    print('Optimal train swapping takes {0} swaps.'.format(solve(n)))
    swaps = 0 #since swaps is a global variable we have to reset it after each print in order to have the exact amount of swaps and not the last solution and the actual added
    cases -= 1

main()

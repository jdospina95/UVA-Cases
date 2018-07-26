from sys import stdin

tab = [[ -1 for i in range (51)] for j in range (51)]
cutting = [ None for i in range(51)]

def solve(left, right, leftindex, rightindex):
    global tab, cutting
    
    # left: left section of the rod
    # right: right section of the rod 
    # leftindex: the leftmost edge of the cutting point to be used as index
    # rightindex: The rightmost point of the cutting point to be used as index
    
    length = right - left
    if (leftindex == rightindex): return length # only one point to be cut
    elif (leftindex > rightindex): return 0 # There are no possible cutting points so I return 0
    elif (tab[leftindex][rightindex] != float('inf')): return tab[leftindex][rightindex] # When the data has already been changed in the tab
    i = leftindex
    while (i <= rightindex): # start filling the memory (tab) with the minimun value up to i, as seen in class
        tab[leftindex][rightindex] = min(tab[leftindex][rightindex], solve(left, cutting[i], leftindex, i - 1) + solve(cutting[i], right, i + 1, rightindex) + length) 
        i += 1
    return tab[leftindex][rightindex] # The result is stored in the last position of tab where leftindex and rightindex = left and right respectively
    
def main():
    global cutting, tab
    
    inp = stdin
    l = int(inp.readline())
    while (l != 0): # l = 0 end of input
        n = int(inp.readline()) # number of cuts to be made
        tok = inp.readline().strip().split() # places where the cuts need to be done
        for i in range(n): cutting[i] = int(tok[i]) # assign all the cutting points into the list
        for i in range(0,51):
            for j in range(0,51):
                tab[i][j] = float('inf') # Reset the tab to be all in the greatest value possible (infinite)
        print('The minimum cutting is {0}.'.format(solve(0, l, 0, n - 1)))
        l = int(inp.readline())
        

main()

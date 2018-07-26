from sys import stdin

def solve(missiles):
    
    l = len(missiles)
    
    tab = [ 1 for x in range(l) ] # create a tab and initialize it in 1 to store the temp answer
    tab[0] = 2 # assign a greater value in the first position so that the first condition inside the while will be evaluated in the first iteration
    
    for i in range(1, l):
        j = 0
        maximum = 0
        while j < i+1:
            if (missiles[i] <= missiles[j] and maximum < tab[j]+1): # assign the sequence to maximum so I know how many missiles have been caught
                maximum = tab[j]+1
            else: j+=1
        tab[i] = maximum # store the max sequence found with the element in the position i according to the iteration

    return max(tab) #returns the maximum sequence found, it is returned as max since we need the maximun number of missiles caught
    
def main():
    inp = stdin
    line = int(inp.readline())
    testcase = 1
    while (line != -1): # iterate over the input as long as it reads a line different from -1 for a test case
        missiles = [] # list which will contain all the data for the missiles
        missiles.append(int(line))
        line2 = int(inp.readline())
        while (line2 != -1): # iterate until it finds a -1 so that each test case is separated
            missiles.append(int(line2))
            line2 = int(inp.readline())
        if (testcase > 1):
            print ()
        print ('Test #{0}:'.format(testcase))
        print ('  maximum possible interceptions:', solve(missiles)-1)
        line = int(inp.readline())
        testcase += 1
    
main()

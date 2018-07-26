from sys import stdin

MAX = 100001 #MAX value for the inputs according to the problem
jackpot = [ None for i in range(MAX) ] #The array which will contain all the possible bets, filled with none type values as you explained in class

def solve(array):
    best = current = 0
    for i in array:
        current = max(current + i, 0) #compares the current value of the sum plus the element of the list from the iteration to see if it is greater than 0, if it is negative it assigns 0 to the current value
        best = max(best, current) #the same as before but this compares the actual best value with the value the sum has until that iteration, assigns the best of them to the variable
    return best

def main():
    global jackpot
    inp = stdin
    n = int(inp.readline().strip()) #n takes the value of the length of the list (all the bets)
    while (n != 0):
        tok = inp.readline().strip().split()
        for i in range(n): jackpot[i] = int(tok[i]) #store all the posible plays into the array jackpot which contains all the bets
        if (all(item <= 0 for item in jackpot[0:n])): print ('Losing streak.') #if there is no winning possibility then print that it is a losing streak
        else: print('The maximum winning streak is {0}.'.format(solve(jackpot[0:n])))
        n = int(inp.readline().strip()) #n takes the value of the length of the list (all the bets)

main()

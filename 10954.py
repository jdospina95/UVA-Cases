from sys import stdin
from heapq import heappush, heappop, heapify


def solve(N, numbers):
    total, cost = 0, 0 #Variables to know the total cost of all the summation and the cost of each one separately
    heapify(numbers) #Transform numbers into a heap, in-place, in linear time.
    while (len(numbers) > 1):
        total = numbers[0] #the total cost will be the top element of the priority queue
        heappop(numbers) #Pop and return the smallest item from the heap, maintaining the heap invariant.
        total += numbers[0] #Since the addition is made up of two numbers we have to add the two numbers to know the cost of the summation
        heappop(numbers) #Pop the second smallest number
        cost += total #Total cost
        heappush(numbers, total) #We add to the heap the total cost of the addition of those two elements in order to have it as a new number in the heap
        
    return cost
    
def main():
    inp = stdin
    N = int(inp.readline().strip())
    while (N != 0):
        numbers = []
        tok = inp.readline().strip().split()
        for i in range(len(tok)): numbers.append(int(tok[i]))
        print (solve(N, numbers))
        N = int(inp.readline().strip())
    
main()

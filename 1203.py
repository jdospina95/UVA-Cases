from sys import stdin
from heapq import heappush, heappop

def main():
    inp = stdin
    heap = []
    line = inp.readline().strip().split()
    s, qnum, p = line[0], int(line[1]), int(line[2])
    while (s!='#'):
        qnum, p = int(line[1]), int(line[2])
        heappush(heap, [p,[qnum,p]]) #push the elements into the queue organized with the task and the period for each one, [period,[task,period]]
        line = inp.readline().strip().split()
        s = line[0]
    
    k = int(inp.readline().strip()) #number of queries to be performed
    
    while (k > 0):
        aux = heap[0] #auxiliar "queue" which will contain the top element of the original queue
        heappop(heap) #remove the element
        print (aux[1][0]) #print the second element in the first position (querie number)
        aux[0] += aux[1][1] #the aux heap will now increment it's value with the period of the second element
        heappush(heap, aux) #push the aux with it's modified value into the original queue
        k -= 1
    
    
main()

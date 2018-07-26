from sys import stdin, stdout
import re
from collections import deque

def solve(line):
    line2 = re.findall(r"[\w']+", line) #Split the line into a list with all the elements except for the brackets
    flag = False #flag True = appendLeft else appendRight
    flag2 = False #flag2 False when there is no node to insert after in the begining, True when there ir
    flag3 = True #just insert when we find a new element from list2 not from list
    j = 0
    
    heap = deque()
    for i in line:
        if (i == '['):
            flag = True
            flag2 = False
            flag3 = True
        elif(i == ']'):
            flag = False
            flag3 = True
        else:
            if (flag3):
                flag3 = False
                if (flag): 
                    if (flag2):
                        heap.append(line2[j]) #append the element in list in j position and then add 1 to j
                        j += 1
                    else:
                        heap.appendleft(line2[j]) #append to the left the element in list in j position and then add 1 to j
                        j += 1
                        flag2 = True
                else:
                    heap.append(line2[j])
                    j += 1
    
    for i in range(len(heap)):
        stdout.write (heap[i])

def main():
    inp = stdin
    for line in inp:
        solve(line.strip())
        print()
    
main()

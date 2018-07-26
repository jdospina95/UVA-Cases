from sys import stdin

MAX = 1005
tab = [[ 0 for n in range(MAX) ] for m in range(MAX) ]
list1 = list2 = [ None for x in range(MAX) ]
len1 = len2 = 0

def solve():
    global list1, list2, tab, len1, len2
    
    
    # phi(m,n) : minimun number of operations over list1 and list2 in order for them to be the same
    # Objective - phi(M,N)
    
    # phi(m,n) - case m = 0                                               n
    #          - case n = 0                                               m
    #          - case n!=0 and m!=0 and list1[i-1] == list2[j-1]          phi(i-1, j-1)
    #          - case n!=0 and m!=0 and list1[i-1] != list2[j-1]          min((i-1, j-1), (i-1, j), (i, j-1))+1
             
    # INVARIANTS
    #         P0:     V i,j / 0 <= 1 <= m and 0 <= j <= N: tab[i][j] = phi(i,j)
    #         P1:     V j   / 0 <= j <= n : tab[m][j] = phi(m, j)
    #         P2:     0 <= m <= M
    #         P3:     0 <= n <= N
    
    
    len3 = max(len1, len2) # assign the max length between the length of both lists
    i = 1
    while (i <= len3):
        tab[i][0] = tab[0][i] = i
        i += 1
    
    i = 0
    while (i < len1):
        j = 0
        while (j < len2):
            if (list1[i] == list2[j]): tab[i+1][j+1] = min(tab[i+1][j]+1, tab[i][j+1]+1, tab[i][j])
            else: tab[i+1][j+1] = min(tab[i+1][j]+1, tab[i][j+1]+1, tab[i][j]+1)
            j += 1
        i += 1
    
    return tab[len1][len2]

def main():
    global list1, list2, len1, len2
    inp = stdin
    for line in inp: #Since I don't know how many lines the input has and the sample input has no cases, I read line by line and store the data into a temp
        temp = line.strip().split()
        len1 = int(temp[0]) #the first part of the line input has the length of the array
        list1 = temp[1] #contains the array
        temp = inp.readline().strip().split() #read next line since each case has two lines
        len2 = int(temp[0])
        list2 = temp[1]
        print (solve())
    
main()

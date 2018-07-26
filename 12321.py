from sys import stdin

def solve(a, L, G):
    pos, aux, i, ans = 0, 0, 0, G
    while (pos < L):
        aux = pos
        
        while (i < G and a[i][0] <= pos):
            aux = max(aux,a[i][1])
            i += 1
            
        
        if (aux == pos): break
        
        pos = aux
        ans -= 1
    if (pos < L): return -1
    else: return ans

def main():
    inp = stdin
    L, G = [ int(x) for x in stdin.readline().strip().split() ]
    while (L+G!= 0):
        a = [None for i in range(G)]
        for i in range(G):
            aux1, aux2 = [ int(x) for x in stdin.readline().strip().split() ]
            a[i] = (aux1-aux2,aux1+aux2)
        a.sort()
        print (solve(a, L, G))
        L, G = [ int(x) for x in stdin.readline().strip().split() ]
    
main()

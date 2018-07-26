from sys import stdin

def solve(seen):
    forest = set() #Create a set to be the forest
    for element in seen:
        forest.add(tuple(element)) #adds the ones who were seen
    return (len(forest))


def main():
    inp = stdin
    cases = int(inp.readline().strip())
    inp.readline()
    while (cases != 0):
        line = inp.readline().strip().split()
        people, trees = int(line[0]), int(line[1])
        seen = [[0 for i in range(trees)] for i in range(people)] #Create a table to assign the value 1 to the person and tree tuple so we know which ones were seen falling
        line = inp.readline().strip().split()
        if (line):
            while (line):
                person, tree = int(line[0]), int(line[1])
                seen[person-1][tree-1] = 1 #Person saw the tree fall, assign value 1
                line = inp.readline().strip().split()
            print(solve(seen))
        else: 
            print (1)
        cases -= 1
        if (cases != 0): print ()
    
main()

from sys import stdin, stdout
from collections import defaultdict

def main ():
    inp = stdin
    dictionary = defaultdict(list)
    line = inp.readline()
    while (line != '\n'):
        line = line.strip().split()
        dictionary[line[1]].append(line[0]) #add the key and the value to the dictionary
        line = inp.readline()
        
    for line2 in inp:
        line = line2.strip() #get rid of the '\n'
        if (dictionary[line]): print (str(dictionary[line]).strip("[]").replace("'","")) #If the key returns something then I assume the value exists in the dictionary and then I print it
        else: print('eh') #If the value is not in the dictionary I print eh as said in the problem

main()

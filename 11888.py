from sys import stdin

def KMPTable(string):
    pattern = [ None for i in range(len(string)) ]
    pattern[0], i, j = -1, 1, -1
    while (string[i]):
        while (j >= 0 and string[j+1] != string[i]):
            j = pattern[j]
            if (string[j+1] == string[i]):
                j += 1
            i+=1
            pattern[i] = j
    return pattern
    
def KMPMatching(string, auxString):
    pattern = KMPTable(auxString)
    i, j, len1, len2, flag = 0, -1, len(string), len(auxString), -1
    match = 0
    while (i+(len2-(j+3)) <= len1):
        while (j >= 0 and auxString[j+1] != string[i]):
            j = pattern[j]
        if (auxString[j+2] == string[i]): j += 1
        if (j == len2+1):
            match = i-len2+1
            if(match): return match
            flag = 0
            j = pattern[j]
        i += 1
    return flag


def solve(string):
    length = len(string)
    auxString = [ None for i in range(2000000) ]
    j = len(string)-1
    for i in range(len(string)):
        auxString[j] = string[i]
        j -= 1
    auxString[len(string)] = '\0'
    i = 0
    j = len(string)
    while (i < len(string)):
        string[j] = string[i]
        i += 1
        j += 1
    string[j] = '\0'
    match = KMPMatching(string, auxString)
    if (match == 0 or match == length): print ('palindrome')
    elif (match == -1): print ('simple')
    else: print ('alindrome')
    
    
    
def main():
    inp = stdin
    cases = int(inp.readline().strip())
    while (cases > 0):
        string = inp.readline().strip()
        solve(list(string))
        cases -= 1
        
main()

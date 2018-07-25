from sys import stdin

price = None

def solve(n,m):
  global price
  ans = [0,1000001] #ans is a list where the solution will be stored at. ans[0] will be the best minimun price for one book and ans[1] 
                    #will be the best maximun price for the other book in order for their prices to add up to the amount of money he has
  i = 0
  
  price.sort() #The list will be sorted in order to have the books ordered by prices making it easier to find the correct answer, books prices being the closest possible
  n -= 1
  while i < n:
    if (price[i] + price[n] < m): #if the addition of the prices of the books from all the way to the left and all the way to the right are smaller than the money he has then 
                                  #the next cheap book will be added with the expensive one in n position during the next iteration.
      i += 1
    elif (price[i] + price[n] == m): #if the addition of the prices of the books from all the way to the left and all the way to the right are equal to the money then:
      ans[0] = price[i] #ans in it's first position will store the cheap book's price
      ans[1] = price[n] #ans in it's second position will store the expensive book's price (expensive amongst the two of them)
      i += 1 #the cheap book price position is moved to the right
      n -= 1 #the expensive book price position is moved to the left
    else: #if none of the above conditions are satisfied then:
      n -= 1 #expensive book price position is moved to the left
  return ans


def main():
  global price
  inp = stdin
  line = inp.readline().strip()
  while len(line)>0:
    n = int(line) # amount of books
    price = [ int(x) for x in inp.readline().strip().split() ] # individual book prices
    m = int(inp.readline().strip()) # amount of money
    ans = solve(n,m)
    print('Peter should buy books whose prices are {0} and {1}.\n'.format(ans[0],ans[1]))
    inp.readline()
    line = inp.readline().strip()

main()

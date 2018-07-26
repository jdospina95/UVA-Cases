from sys import stdin
from itertools import product, combinations, tee

class point(object):
    # Create a class called point and assign x and y values on init for the point coordinates
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "%s,%s" % (self.x, self.y)

    def __str__(self):
        return "%s,%s" % (self.x, self.y)


def onSegment(p,q,r):
    # Given three colinear points p, q, r, the function checks if
    # point q lies on line segment 'pr'
    if (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y)):
        return True
    return False
    
def orientation(p,q,r):
    # To find orientation of ordered triplet (p, q, r).
    # The function returns following values
    # 0 --> p, q and r are colinear
    # 1 --> Clockwise
    # 2 --> Counterclockwise
    val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
    if (val == 0): 
        return 0
    if (val > 0):
        return 1
    else:
        return 2

def doIntersect(p1,q1,p2,q2):
    #determine if line segment from a to b intersects with line segment from c to d
    #returns true if line segment 'p1q1' and 'p2q2' intersect.
    
    #Find the four orientations needed for general and special cases
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    
    #General case
    if (o1 != o2 and o3 != o4):
        return True
    
    # Special Cases
    # p1, q1 and p2 are colinear and p2 lies on segment p1q1
    if (o1 == 0 and onSegment(p1, p2, q1)):
        return True
        
    # p1, q1 and p2 are colinear and q2 lies on segment p1q1
    if (o2 == 0 and onSegment(p1, q2, q1)): 
        return True
        
    # p2, q2 and p1 are colinear and p1 lies on segment p2q2
    if (o3 == 0 and onSegment(p2, p1, q2)):
        return True
        
    # p2, q2 and q1 are colinear and q1 lies on segment p2q2
    if (o4 == 0 and onSegment(p2, q1, q2)):
        return True
        
    # doesn't fall in any of the above cases so we assume both line segments do not intersect
    return False 

def isInside(x,y,poly):
    # Given a point and a polygon returns True if the point lies inside the polygon
    # or False if it does not

    n = len(poly) 
    inside = False # Boolean to store if the point lies inside the polygon or not

    p1x,p1y = poly[0].x, poly[0].y # Store the values of x and y for the first point of the polygon
    for i in range(n+1): # Iter over all the points in the polygon
        p2x,p2y = poly[i % n].x, poly[i % n].y # Store the values of x and y for each point of the polygon
        if y > min(p1y,p2y): 
            if y <= max(p1y,p2y):
                # if the y coordinate of the given point is greater than the minimum value between 
                # y coordinates of the first and second point of the polygon, plus being smaller than the max value of
                # y coordinates then we can conclude the point lies inside the y segment
                if x <= max(p1x,p2x): # Check if the given point x is smaller or equal than the max between x coordinates in bot polygon's points
                    if p1y != p2y: # If both polygon's points are different
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x # intersects
                    if p1x == p2x or x <= xinters: # If both points are the same or x is smaller than xinters
                        inside = not inside # Change the boolean value
        p1x,p1y = p2x,p2y # Assign new points for next iteration

    return inside

def findSet(x):
    if (p[x] == x):
        return x
    else:
        p[x] = findSet(p[x])
        return p[x]
        
def union(i,j):
    p[findSet(i)] = findSet(j) # assign a new parent point into the parents list
    
def solve():
    global polygons, p
    
    for i in range(len(polygons)): # iterate over all the different polygons in the test case
        for j in range(i+1, len(polygons)): # iterate over all the different polygons in the test case but starting from the second, in order to make comparations between polygons i and j
            for a in range(len(polygons[i])):
                if (isInside(polygons[i][a].x, polygons[i][a].y, polygons[j])):
                    union(i,j)
            for a in range(len(polygons[j])):
                if (isInside(polygons[j][a].x, polygons[j][a].y, polygons[i])):
                    union(i,j)
            
            for a in range(len(polygons[i])): # iterate over all the different points in the polygon i
                for b in range(len(polygons[j])): # iterate over all the different points in the polygon j
                    if(doIntersect(polygons[i][a], polygons[i][(a+1)%len(polygons[i])],polygons[j][b], polygons[j][(b+1)%len(polygons[j])])): # check if every single pair of line segments, each one made up of two points, intersect with each other
                        union(i,j) # the two line segments intersect so we join them by using union
                        break 
    
    ans = []
    for i in range(len(polygons)): ans.append(findSet(i)) # store all the polygons parents into ans
    
    return len(set(ans)) # by returning a set I remove all the repeated parents
                         # i.e. 3,3 and 4,4 parent is point with id 1 then it will just
                         # count point with 1 once and not twice

def main():
    global polygons, p
    inp = stdin
    n = int(inp.readline().strip())
    while (n!=0):
        p = [ i for i in range(n)] # list to store all the different parents for the points, each parent is represented with a number from 0...n-1 representing the polygons
        polygonsaux, polygons = [], [] # list to store all the points of one polygon and then append the aux into polygons to have all the polygons points stored
        for i in range(n):
            aux = stdin.readline().strip().split()
            aux2 = [ None for i in range(len(aux))]
            for j in range(len(aux)-1):
                if j%2==0: aux2[j] = point(int(aux[j]), int(aux[j+1])) # store points by pairs, do not repeat a point in a different pair
            for x in range(len(aux2)): 
                if aux2[x]!= None: polygonsaux.append(aux2[x])
            polygons.append(polygonsaux) # append the polygon's point into the list that contains all the polygons for the current test case
            polygonsaux = []
        print(solve())
        n = int(inp.readline().strip())
        
main()

import math
def is_square(p1,p2,p3,p4):
    pts=[p1,p2,p3,p4]
    dist=set()
    for i in range(4):
        for j in range(i+1,4):
            d=math.sqrt((pts[i][0]-pts[j][0])**2 - (pts[i][1]-pts[j][1])**2)
            dist.add(d)
    lt=list(dist)
    dist.sort()
    side=dist[0]
    diag=dist[1]
    if len(dist)==2 and 0 not in dist and diag**2==2*side**2:
        return True
    else:
        return False

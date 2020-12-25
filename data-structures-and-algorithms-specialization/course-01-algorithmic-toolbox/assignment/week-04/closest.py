#Uses python3
import sys
import math

def dist(i, j):
    return math.sqrt(math.pow(i[0] - j[0], 2) + math.pow(i[1] - j[1], 2))

def minimum_distance(pts):
    #write your code here
    if len(pts) == 2:
        return dist(pts[0], pts[1])
    if len(pts) == 3:
        d1 = dist(pts[0], pts[1])
        d2 = dist(pts[0], pts[2])
        d3 = dist(pts[1], pts[2])
        return min(min(d1,d2), d3)
    
    pts.sort()

    d1 = minimum_distance(pts[:len(pts) // 2])
    d2 = minimum_distance(pts[len(pts) // 2:])
    d = min(d1, d2)
    midline = (pts[(len(pts) // 2) - 1][0] + pts[len(pts) // 2][0]) / 2

    filtered_pts = [point for point in pts if abs(point[0] - midline) <= d]
    x = [0] * len(filtered_pts)
    y = [0] * len(filtered_pts)
    for i in range(len(filtered_pts)):
        x[i] = filtered_pts[i][0]
        y[i] = filtered_pts[i][1]

    midpts = [[j,i] for i, j in sorted(zip(y,x))]
    minmid = -1
    for i in range(len(midpts)):
        curpoint = midpts[i]
        j = 1
        while j <= 7 and i + j < len(midpts):
            curdist = dist(curpoint, midpts[i+j])
            if minmid == -1:
                minmid = curdist
            elif minmid > curdist:
                minmid = curdist
            j += 1

    if minmid == -1:
        return d
    
    d = min(d, minmid)
    return d

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    pts = list(zip(x,y))
    print("{0:.9f}".format(minimum_distance(pts)))

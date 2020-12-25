# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    start = []
    end = []
    for s in segments:
        start.append(s.start)
        end.append(s.end)
    data = [(x, y) for x, y in sorted(zip(end, start))]
    while len(data):
        index_to_pop = []
        curpoint = data[0][0]
        points.append(curpoint)
        for i in range(len(data)):
            if curpoint >= data[i][1]:
                index_to_pop.append(i)
            else:
                break
        for idx in sorted(index_to_pop, reverse=True):
            data.pop(idx)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

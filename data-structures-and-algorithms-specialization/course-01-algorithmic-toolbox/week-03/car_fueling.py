# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.insert(0, 0)
    stops.append(distance)
    idx = 0
    numrefill = 0
    while idx < len(stops):
        oldpos = stops[idx]
        while idx < len(stops) and stops[idx] - oldpos <= tank:
            idx += 1
        if idx == len(stops):
            return numrefill
        idx -= 1
        if oldpos == stops[idx]:
            return -1
        numrefill += 1
    return numrefill

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))

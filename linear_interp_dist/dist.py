from bisect import bisect_left
from random import uniform

def make_lookup(data):
    keys = sorted(data.keys())
    lookup = dict()
    total = 0
    for lkey, hkey in zip(keys, keys[1:]):
        lval, hval = data[lkey], data[hkey]
        total += (lval + hval) * (hkey - lkey) // 2
        lookup[total] = lkey
    return lookup

def draw_number(cprobs, lookup):
    rand = uniform(0, cprobs[-1])
    index = bisect_left(cprobs, rand) - 1
    lo, hi = cprobs[index], cprobs[index+1]
    lkey, hkey = lookup[lo], lookup[hi]
    return lkey + (rand - lo) * (hkey - lkey) / (hi - lo)

def main():
    data = {128.0: 2.63, 130.0: 2.46, 107.0: 6.13, 98.4: 8.54, 135.0: 2.1, 138.0: 1.94, 87.3: 12.5, 142.0: 1.73, 60.7: 13.7, 61.4: 15.7, 150.0: 1.34, 117.0: 3.92, 154.0: 1.18, 111.0: 5.24, 60.1: 12.1, 90.1: 11.5, 99.9: 8.03, 163.0: 0.91, 146.0: 1.52, 62.9: 18.7, 172.0: 0.712, 45.0: 0.263, 47.3: 0.47, 51.5: 1.34, 180.0: 0.592, 57.1: 4.89, 54.3: 2.35, 55.1: 2.84, 56.6: 4.36, 57.9: 6.41, 58.4: 7.46, 59.6: 10.6, 60.6: 14.2, 61.2: 15.2, 62.7: 18.3, 53.0: 1.86, 64.7: 19.8, 67.3: 19.8, 68.3: 19.3, 69.4: 18.8, 70.4: 18.3, 71.5: 17.8, 72.8: 17.3, 74.0: 16.8, 75.6: 16.4, 77.2: 15.9, 78.2: 15.4, 79.7: 14.9, 56.1: 3.88, 82.9: 13.9, 58.6: 7.98, 84.7: 13.4, 86.0: 13.0, 57.4: 5.41, 89.1: 12.0, 57.6: 5.9, 91.7: 11.0, 92.9: 10.5, 58.1: 6.97, 94.2: 9.99, 95.8: 9.52, 96.8: 9.04, 62.4: 17.8, 59.1: 8.99, 101.0: 7.59, 81.3: 14.4, 60.9: 14.7, 103.0: 7.08, 109.0: 5.66, 61.7: 16.2, 112.0: 4.74, 59.9: 11.6, 62.2: 17.2, 105.0: 6.61, 55.8: 3.39, 122.0: 3.32, 63.7: 19.3, 124.0: 3.12}

    lookup = make_lookup(data)
    cprobs = sorted(lookup.keys())

    num = draw_number(cprobs, lookup)
    print(num)

if __name__ == "__main__":
    main()

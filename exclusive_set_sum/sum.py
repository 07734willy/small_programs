from itertools import combinations, product
from random import uniform

@profile
def solve(const_dict, m):
    pairs = sorted(const_dict.items(), key=lambda x: x[1])
    lookup = {comb:i for i, (comb, _) in enumerate(pairs)}
    #pairs = [(set(comb), val) for comb, val in pairs]
    #min_sums = [(set(comb), val) for comb, val in pairs]
    min_sums = list(pairs)
    pairs = [(set(comb), val) for comb, val in pairs]
    #print(min_sums)
    #print("===============")

    for _ in range(1, m):
        new_sums = []
        for comb, val in min_sums:
            idx = lookup[comb[-4:]] + 1
            set_comb = set(comb)
            min_comb, min_val = None, None
            for j in range(idx, len(pairs)):
                #c, v = pairs[j]
                #if not c & set_comb:
                if not pairs[j][0] & set_comb:
                    new_sums.append((comb + tuple(sorted(x for x in pairs[j][0])), val + pairs[j][1]))
                    #new_sums.append((comb + tuple(sorted(x for x in c)), val + v))
                    break
        min_sums = sorted(new_sums, key=lambda x: x[1])
    return min_sums[0]

def brute(const_dict, m):
    pairs = sorted(const_dict.items(), key=lambda x: x[1])
    min_sums = [tuple(zip(*x)) for x in product(*([pairs] * m))]
    min_sums = [(tuple(c for co in comb for c in co), sum(v for v in val)) for comb, val in min_sums]
    min_sums = [(comb, val) for comb, val in min_sums if len(comb) == len(set(comb))]
    #, key=lambda x: sum(y[1] for y in x))
    return min(min_sums, key=lambda x: x[1])

def main():
    n = 20
    m = 5
    lower, upper = 5, 10

    const_dict = dict()
    for comb in combinations(range(n), 4):
        const_dict[comb] = uniform(lower, upper)

    smallest = solve(const_dict, m)
    print(smallest)
    #print(brute(const_dict, m))

if __name__ == "__main__":
    main()

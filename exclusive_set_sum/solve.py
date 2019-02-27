from itertools import combinations, product
from random import uniform

#@profile
def solve(const_dict, n, m):

    #pairs = sorted(const_dict.items(), key=lambda x: x[1])
    #lookup = {comb:i for i, (comb, _) in enumerate(pairs)}
    lookup = {comb:(comb,) for comb in const_dict.keys()}

    keys = set(range(n))
    for size in range(8, 4 * m + 1, 4):
        for key_total in combinations(keys, size):
            key_set = set(key_total)
            min_keys = (key_total[:4], key_total[4:])
            min_val = const_dict[min_keys[0]] + const_dict[min_keys[1]]
            #for key1, key2 in zip(combinations(key_total, 4), reversed(list(combinations(key_total, size - 4)))):
            #    #key2 = tuple(sorted(x for x in key_set - set(key1)))
            #    #key2 = tuple(x for x in key_total if x not in key1)
                
            #    if min_val > const_dict[key1] + const_dict[key2]:
            #        min_keys, min_val = (key1, key2), const_dict[key1] + const_dict[key2]
            key1, key2 = min(zip(combinations(key_total, 4), reversed(list(combinations(key_total, size - 4)))), key=lambda x:const_dict[x[0]]+const_dict[x[1]])
            #key1, key2 = min(zip(combinations(key_total, 4), reversed(list(combinations(key_total, size - 4)))), key=lambda x:sum(const_dict[y] for y in x))
            
            #min_keys, min_val = (key1, key2), const_dict[key1] + const_dict[key2]

            #k = tuple(sorted(x for key in min_keys for x in key))
            #const_dict[k] = min_val
            #lookup[k] = lookup[min_keys[0]] + lookup[min_keys[1]]
            k = tuple(sorted(x for x in key1 + key2))
            const_dict[k] = const_dict[key1] + const_dict[key2]
            lookup[k] = lookup[key1] + lookup[key2]


            #print(k, min_val, lookup[k])

    key, val = min(((key, val) for key, val in const_dict.items() if len(key) == 4 * m), key=lambda x: x[1])
    return lookup[key], val

def solve2(const_dict, n, m):

    #pairs = sorted(const_dict.items(), key=lambda x: x[1])
    #lookup = {comb:i for i, (comb, _) in enumerate(pairs)}
    lookup = {comb:(comb,) for comb in const_dict.keys()}

    keys = set(range(n))
    for size in range(8, 4 * m + 1, 4):
        for key1 in combinations(keys, 4):
            #key_set = keys - set(key1)
            key_tup = tuple(sorted(x for x in keys - set(key1)))
            
            for key2 in combinations(key_tup, size - 4):
                
                val = const_dict[key1] + const_dict[key2]
                key = tuple(set(key1 + key2))
                if key not in const_dict or const_dict[key] > val:
                    const_dict[key] = val
                    lookup[key] = lookup[key1] + lookup[key2]
            
            #print(k, min_val, lookup[k])

    key, val = min(((key, val) for key, val in const_dict.items() if len(key) == 4 * m), key=lambda x: x[1])
    return lookup[key], val

def main():
    n = 18
    m = 4
    lower, upper = 5, 10

    const_dict = dict()
    for comb in combinations(range(n), 4):
        const_dict[comb] = uniform(lower, upper)

    result = solve(const_dict, n, m)
    print(result)

if __name__ == "__main__":
    main()

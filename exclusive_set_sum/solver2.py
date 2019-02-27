from itertools import combinations
from random import uniform

def solve(const_dict, n, m, extra_runs=10, check_factor=2):
    pairs = sorted(const_dict.items(), key=lambda x: x[1])

    lookup = [set([]) for _ in range(n)]
    nset = set([])

    min_sums = []
    min_key, min_val = None, None
    for i, (pkey, pval) in enumerate(pairs):
        valid = set(nset)
        for x in pkey:
            valid -= lookup[x]
            lookup[x].add(len(min_sums))
        
        nset.add(len(min_sums))
        min_sums.append(((pkey,), pval))

        for x in pkey:
            lookup[x].update(range(len(min_sums), len(min_sums) + len(valid)))
        for idx in valid:
            comb, val = min_sums[idx]
            for key in comb:
                for x in key:
                    lookup[x].add(len(min_sums))
            nset.add(len(min_sums))
            min_sums.append((comb + (pkey,), val + pval))
            if len(comb) == m - 1 and (not min_key or min_val > val + pval):
                min_key, min_val = min_sums[-1]
        
        if min_key:
            if not extra_runs: break
            extra_runs -= 1

    for pkey, pval in pairs[:int(check_factor*i)]:
        valid = set(nset)
        for x in pkey:
            valid -= lookup[x]
        
        for idx in valid:
            comb, val = min_sums[idx]
            if len(comb) < m - 1:
                nset.remove(idx)
            elif min_val > val + pval:
                min_key, min_val = comb + (pkey,), val + pval
    return min_key, min_val

def dp_solve(const_dict, n, m):

    lookup = {comb:(comb,) for comb in const_dict.keys()}

    keys = set(range(n))
    for size in range(8, 4 * m + 1, 4):
        for key_total in combinations(keys, size):
            key_set = set(key_total)
            min_keys = (key_total[:4], key_total[4:])
            min_val = const_dict[min_keys[0]] + const_dict[min_keys[1]]

            key1, key2 = min(zip(combinations(key_total, 4), reversed(list(combinations(key_total, size - 4)))), key=lambda x:const_dict[x[0]]+const_dict[x[1]])

            k = tuple(sorted(x for x in key1 + key2))
            const_dict[k] = const_dict[key1] + const_dict[key2]
            lookup[k] = lookup[key1] + lookup[key2]

    key, val = min(((key, val) for key, val in const_dict.items() if len(key) == 4 * m), key=lambda x: x[1])
    return lookup[key], val



def solve2(const_dict, n, m):
    pairs = sorted(const_dict.items(), key=lambda x: x[1])

    lookup = [set([]) for _ in range(n)]
    nsetA = set([])
    nsetB = set([])

    min_sums = [] #[((tuple(),), 0)]
    for i, (pkey, pval) in enumerate(pairs):
        nset, nset_other = (nsetA, nsetB) if i & 1 else (nsetB, nsetA)
        valid = set(nset)
        for x in pkey:
            valid -= lookup[x]
            lookup[x].add(len(min_sums))
        
        nset.add(len(min_sums))
        min_sums.append(((pkey,), pval))

        for idx in valid:
            comb, val = min_sums[idx]
            valid_other = set(nset_other)
            for key in comb + (pkey,):
                for x in key:
                    valid_other -= lookup[x]
                    lookup[x].add(len(min_sums))

            nset.add(len(min_sums))
            min_sums.append((comb + (pkey,), val + pval))
            if len(comb) == m - 1:
                return min_sums[-1]

            for idx_other in valid_other:
                if len(min_sums[idx_other][0]) + len(comb) == m - 1:
                    k, v = min_sums[idx_other]
                    return k + comb + (pkey,), v + val + pval



def main():
    n = 24
    m = 6
    lower, upper = 5, 10

    for _ in range(10):
        const_dict = dict()
        for comb in combinations(range(n), 4):
            const_dict[comb] = uniform(lower, upper)
        
        smallest = solve(const_dict, n, m)
        print(smallest)
        smallest = solve(const_dict, n, m, 0, 0)
        print(smallest)
    """
    counter = 0
    smallest = smallest3 = [0, 0]
    while smallest[1] == smallest3[1]:
        const_dict = dict()
        for comb in combinations(range(n), 4):
            const_dict[comb] = uniform(lower, upper)
    
        smallest = solve(const_dict, n, m)
        smallest3 = solve3(const_dict, n, m)
        counter += 1
    print(smallest)
    print(smallest3)
    print(counter)
    """

if __name__ == "__main__":
    main()

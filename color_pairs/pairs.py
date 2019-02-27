from itertools import combinations, permutations
from random import shuffle

def get_subsets(color_set):
    subsets = []
    for d in ({}, {'1':'5'}, {'4':'6'}, {'1':'5', '4':'6'}):
        tr = lambda s: str.translate(s, str.maketrans(d))
        subsets.extend(set(tr(y) for y in x) for x in combinations(color_set, 3))
    return subsets

def make_sets(do_random=True):
    color_sets = [set(c+str(i) for i, c in enumerate(perm)) for perm in permutations("RGBYPOW")]
    
    results, pairs = [], []
    while color_sets:
        results.append(color_sets[0])
        pairs.extend(get_subsets(color_sets[0]))
        color_sets = [x for x in color_sets if all(y - x for y in pairs)]
        if do_random: shuffle(color_sets)
    
    results = sorted(sorted(perm, key=lambda x:x[1]) for perm in results)
    print("\n".join(map(str, results)))
    print(len(results))

if __name__ == "__main__":
    make_sets()

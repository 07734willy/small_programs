from random import randint, seed
from itertools import product, combinations, chain
from collections import defaultdict

def split_full_meshes(meshes=[[0,1,2],[0,1,3]], broken_edge=[0,1]):
    nu_meshes = []
    for mesh in meshes:
        if broken_edge[0] in mesh and broken_edge[1] in mesh:
            for node in broken_edge:
                nu_meshes.append([i for i in mesh if i!= node])
        else:
            nu_meshes.append(list(mesh))
            #nu_meshes.append(np.copy(mesh))
    return nu_meshes


def maximal_full_mesh(a=[2,2,3,4], broken_edges=[[0,1],[2,3]]):
    meshes = [list(range(len(a)))]
    for ed in broken_edges:
        meshes_tmp = [list(x) for x in meshes] #np.copy(meshes)
        meshes = split_full_meshes(meshes_tmp, ed)
    max_mesh = 0
    for mesh in meshes:
        max_mesh = max(max_mesh, sum(a[x] for x in mesh))
        #max_mesh = max(max_mesh, sum(a[np.array(mesh)]))
    return max_mesh


def solve2(pairs, to_search, d):
    if not to_search: return [[]]

    a, b = pairs[next(iter(to_search))]
    result  = [[a] + r for r in solve(pairs, to_search - d[a], d)] or [[a]]
    result += [[b] + r for r in solve(pairs, to_search - d[b], d)] or [[b]]
    #print(result)
    return result

class FullMesh:
    def __init__(self, weights, pairs=[]):
        self.weights = weights
        self.elements = set(range(len(weights)))
        self.set_pairs(pairs)

    def set_pairs(self, pairs):
        self.pairs = pairs
        self.skips = {e:set() for e in self.elements}
        for i, (a, b) in enumerate(pairs):
            self.skips[a].add(i)
            self.skips[b].add(i)

    def powerset(self, elements):
        return chain.from_iterable(combinations(elements, r) for r in range(len(elements)+1))

    @profile
    def find_all(self):
        to_search = self.powerset(list(combinations(self.elements, 2)))
        pairs_searched = dict()
        for pairs in to_search:
            if pairs in pairs_searched: continue
            
            self.set_pairs(pairs)
            val, nums = self.find_max()
            
            new_pairs = set(product(set(self.elements) - set(nums), set(self.elements))) - set(pairs)
            new_pairs = {(x, y) for x, y in new_pairs if x < y}
            new_pairs = self.powerset(new_pairs)
            #pairs_searched[pairs] = (val, nums)
            #for np in new_pairs:
            #    pairs_searched[tuple(sorted(pairs + np))] = (val, nums)
            pairs_searched.update({tuple(sorted(pairs + np)):(val,nums) for np in new_pairs})
        return pairs_searched
    
    def find_max(self):
        max_score = sum(self.weights)
        val, nums = self.exclude(0, max_score + 1, set(range(len(self.pairs))))
        return max_score - val, sorted(self.elements - set(nums))

    def exclude(self, curr_score, min_score, search):
        if not search or min_score <= curr_score:
            return curr_score, []

        min_nums = []
        for e in self.pairs[next(iter(search))]:
            score, nums = self.exclude(curr_score + self.weights[e], min_score, search - self.skips[e])
            if score < min_score:
                min_score, min_nums = score, nums + [e]
        return min_score, min_nums

def make_pairs(n, m):
    pairs = set()
    while len(pairs) < n:
        a = randint(0, m-1)
        b = randint(0, m-1)
        if a == b: continue
        pairs.add((min(a, b), max(a, b)))
    return list(pairs)

def make_weights(n, w):
    return [randint(0, w-1) for _ in range(n)] 

@profile
def main():
    n, m = 2, 7
    w = 50
    seed(2)
    pairs = make_pairs(n, m)
    weights = make_weights(m, w)
    #print(pairs)
    
    #weights = [0, 8, 2, 4, 1, 6, 0, 2]
    #inp = [[1, 4], [1, 3], [1, 7], [2, 5]]
    all = FullMesh(weights).find_all()
    print("solved")
    #print("\n".join(map(str, all.items())))
    print(len(all))
    for key, value in all.items():
        if value != FullMesh(weights, key).find_max():
            print("DOES NOT MATCH")
            print(key, weights)
            print(value)
            print(FullMesh(weights, key).find_max())
    """
    res = FullMesh(weights, pairs).find_max()
    print(res)
    print("done")
    #print(weights)
    #print(inp)
    #print(*res)
    res2 = maximal_full_mesh(weights, pairs)
    print(res2)
    """

if __name__ == "__main__":
    main()

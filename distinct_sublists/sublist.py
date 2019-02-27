

def maximize_distinct(sublists):
    subsets = [{x for tup in sublist for x in tup} for sublist in sublists]
    
    def intersect(subset):
        return {i for i, sset in enumerate(subsets) if subset & sset}
    
    intersections = [intersect(subset) for subset in subsets]
    weights = [len(subset) for subset in subsets]

    pool = set(range(len(subsets)))
    max_set, _ = search_max(pool, intersections, weights)
    return [sublists[i] for i in max_set]

def search_max(pool, intersections, weights):
    if not pool: return [], 0
    
    max_set = max_weight = None
    for num in pool:
        next_pool = {x for x in pool - intersections[num] if x > num}
        set_ids, weight = search_max(next_pool, intersections, weights)
        
        if max_weight < weight + weights[num] or not max_set:
            max_set, max_weight = [num] + set_ids, weight + weights[num]
    return max_set, max_weight




def main():
    problem = [
        [(1,2,3), (8,9,10), (15,16)],
        [(2,3), (10,11)],
        [(9,10,11), (17,18,19), (20,21,22)],
        [(4,5), (11,12,13), (18,19,20)]
    ]

    print(maximize_distinct(problem))

if __name__ == "__main__":
    main()

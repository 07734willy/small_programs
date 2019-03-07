from collections import Counter, defaultdict
from random import sample, randint, seed
from random import choice, random
from string import ascii_lowercase as ascii
from itertools import combinations
from statistics import pstdev
def main():
    seed(3)
    rand_size = 1000

    subsets = [sample(ascii, randint(1, len(ascii)-1)) for _ in range(rand_size)]
    
    print(subsets)

    lookup = defaultdict(set)
    for idx, subset in enumerate(subsets):
        for character in subset:
            lookup[character].add(idx)

    best_score, best_subsets = 1, None
    size = 10
    subset_indices = set()
    character_subsets = defaultdict(set)
    for _ in range(100):
        if len(subset_indices) > size:
            idx = choice(list(subset_indices))
            if random() < 0.9:
                indices = max(character_subsets.values(), key=len)
                idx = choice(list(indices))
            for character in subsets[idx]:
                character_subsets[character].remove(idx)
            subset_indices.remove(idx)
        else:
            idx = choice(list(set(range(len(subsets))) - subset_indices))
            if random() < 0.9:
                i, indices = min(character_subsets.items(), key=lambda x:len(x[1]), default=(randint(0, len(lookup)-1),set()))
                indices = lookup[i] - indices
                if not indices: continue
                idx = choice(list(indices))
            for character in subsets[idx]:
                character_subsets[character].add(idx)
            subset_indices.add(idx)
        score = pstdev(map(len, character_subsets.values()))
        if score < best_score and len(subset_indices) == size:
            print("indices", subset_indices)
            print("char", character_subsets)
            best_subsets = dict(character_subsets)
            best_score = score

    print(best_subsets)
    print(best_score)

    counter = {x:len(y) for x, y in best_subsets.items()}
    print(counter)
    return best_subsets




if __name__ == "__main__":
    main()

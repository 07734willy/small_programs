from collections import Counter
from heapq import heappushpop, heapify


def get_most_frequent(nums, k):
    counts = Counter(nums)
    counts = [(v, k) for k, v in counts.items()]

    heap = counts[:k]
    heapify(heap)
    
    for count in counts[k:]:
        heappushpop(heap, count)

    return [k for v, k in heap]

def main():
    k = 4
    nums = [1, 2, 1, 1, 3, 2, 3, 3]

    most_freq = get_most_frequent(nums, k)

    print(most_freq)

if __name__ == "__main__":
    main()

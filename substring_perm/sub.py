from collections import defaultdict, Counter

def solve(word, size):
    if len(word) < size:
        return
    
    seen = defaultdict(int)
    seen.update(Counter(word[:size]))
    total = len(seen)

    for i, (v1, v2) in enumerate(zip(word, word[size:])):
        if total == size:
            return i
        
        seen[v1] -= 1
        total -= seen[v1] == 0
        seen[v2] += 1
        total += seen[v2] == 1
    
    if total == size:
        return len(word) - size

def main():
    word = input()
    size = int(input())

    min_index = solve(word, size)
    if min_index != None:
        print("Min index: {}".format(min_index))
    else:
        print("Not possible")
            
if __name__ == "__main__":
    main()

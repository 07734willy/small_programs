from random import randint

def is_valid(m, b, pairs):
    diffs = set()
    for i, (x, y) in enumerate(pairs):
        #diffs.add((y * m - x) % b)
        #diffs.add((y % b) ^ x)
        diffs.add(((y % b) % m) - x)
    if len(diffs) > 1:
        #if len(diffs) < 3:
        #    print(len(diffs))
        return False
    return True

def main():
    pairs = [(435, -150506083839986154),
             (232, -2202615690374524533),
             (29,  -8221824692918245831),
             (0,    8704166314008010995)]
    
    pairs = [(15, -150506083839986154),
             (8, -2202615690374524533),
             (1,  -8221824692918245831),
             (0,    8704166314008010995)]

    px, py = next(iter(pairs))
    while True:
        b = randint(16, 99)
        m = randint(16, b)
        if is_valid(m, b, pairs):
            print(m, b)
            break

if __name__ == "__main__":
    main()

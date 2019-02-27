def main():
    m, n = [int(x) for x in input().split(" ")]
    
    generation = 0
    values = set([n])
    old_values = set([])
    while m not in values:
        new_values = set(x//2 for x in values if not x&1)
        values = new_values | set(x+1 for x in values)
        values -= old_values
        old_values |= values
        generation += 1
    
    print(generation)

if __name__ == "__main__":
    main()



def find_missing(numbers):
    minimum = 1
    length = len(numbers)

    i = 0
    while i < length:
        idx = numbers[i] - minimum
        if idx < length:
            if numbers[i] - minimum == i:
                i += 1
            else:
                numbers[idx], numbers[i] = numbers[i], numbers[idx]
        else:
            numbers[i] = None
            i += 1

    for i, val in enumerate(numbers):
        if val is None: return i + minimum
    return minimum + length

def find_missing2(numbers):
    minimum = 1
    length = len(numbers)

    for i in range(length):
        numbers[i] -= minimum

    for i, val in enumerate(numbers):
        while val != i:
            if val >= length:
                numbers[i] = None
                break

            numbers[val], numbers[i] = val, numbers[val]
            val = numbers[i]

    for i, val in enumerate(numbers):
        if val is None: return i + minimum
    return minimum + length

def find_missing3(numbers):
    for i in range(len(numbers)):
        if numbers[i] >= len(numbers):
            numbers[i] = None
    
    for i in range(len(numbers)):
        while numbers[i] not in (i, None):
            numbers[numbers[i]], numbers[i] = numbers[i], numbers[numbers[i]]
    for i, val in enumerate(numbers[1:], 1):
        if val is None: return i
    return len(numbers)

def main():
    numbers = [3, 2, 1, 7]
    numbers = [4, 2, 7, 6, 1, 3]
    missing = 1#find_missing(list(numbers))
    missing2 = 1#find_missing2(list(numbers))
    missing3 = find_missing3(list(numbers))
    print(missing, missing2, missing3)

if __name__ == "__main__":
    main()

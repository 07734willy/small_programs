from random import randint

def main():
    max_size = int(input())
    n = randint(1, max_size)
    m = randint(1, max_size)
    k = randint(0, 10**9)

    a = [randint(1, 10**9) for _ in range(n)]
    b = [randint(1, 10**9) for _ in range(m)]

    print("{} {} {}".format(n, m, k))
    print(" ".join(map(str, a)))
    print(" ".join(map(str, b)))

if __name__ == "__main__":
    main()

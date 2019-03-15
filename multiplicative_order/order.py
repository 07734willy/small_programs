from math import gcd


def multiplicative_order(a, n):
    if gcd(a, n) != 1:
        return -1

    result = 1
    k = 1
    while k < n:
        result = (result * a) % n

        if result == 1:
            return k

        k += 1
    return -1

def multiplicative_order2(a, n):
    if gcd(a, n) != 1:
        return -1

    visited = {}
    count = 0

    slow = fast = 1
    while fast not in visited:
        visited[slow] = count
        count += 1
        slow = (slow * a) % n
        fast = (fast * slow) % n

    return count * (count + 1) // 2 - visited[fast]

from random import randint
def main():
    n = randint(10, 10000)
    a = randint(7, n)
    order = multiplicative_order(a, n)
    order2 = multiplicative_order2(a, n)
    #print(order)
    #print(order2)
    if order != order2:
        print(n, a)
        print(order, order2)


if __name__ == "__main__":
    print(multiplicative_order(15, 62))
    for _ in range(2000):
        main()

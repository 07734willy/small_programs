

@profile
def atkin_sieve(limit):
    assert limit > 3
    sieve_list = [False] * (limit + 1)
    sieve_list[2:4] = (True, True)

    # Part I: preliminary work
    x = x_squared = 1
    while x_squared < limit:
        y = y_squared = 1
        while y_squared < limit:
            n = 4 * x_squared + y_squared
            if n <= limit and n % 12 in (1, 5):
                sieve_list[n] = not sieve_list[n]

            #n = 3 * x_squared + y_squared
            n -= x_squared
            if n <= limit and n % 12 == 7:
                sieve_list[n] = not sieve_list[n]

            if x > y:
                #n = 3 * x_squared - y_squared
                n -= 2 * y_squared
                if n <= limit and n % 12 == 11:
                    sieve_list[n] = not sieve_list[n]
            y += 1
            y_squared = y * y
        x += 1
        x_squared = x * x

    # Part II: Remove the squares of primes (and their multiples)
    r = 5
    r_squared = r * r
    while r_squared < limit:
        if sieve_list[r]:
            for n in range(r_squared, len(sieve_list), r_squared):
                sieve_list[n] = False
        r += 1
        r_squared = r * r

    # Part III: Append everything into a list
    return [x for x, p in enumerate(sieve_list) if p]


if __name__ == "__main__":
    n = 300000
    primes = atkin_sieve(n)

    #print(primes)

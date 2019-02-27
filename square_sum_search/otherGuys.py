import math
import time

def break3(N):
    count = 0
    z_limit = N // 2
    for z in range(3, z_limit):

        # Since y >= x, there's a lower bound on y
        target = z*z - 1
        ymin = int(math.sqrt(target/2))
        for y in range(ymin, z):
            # Given y and z, compute x.
            # That's a solution iff x is integer.
            x_target = target - y*y
            x = int(math.sqrt(x_target))
            if x*x == x_target and x+y+z <= N:
                print("solution", x, y, z)
                count += 1

    return count


test = [10, 100, 1000, 10**4, 10**5]
border = "-"*20

for case in test: 
    print(border, case)
    start = time.time()
    print(break3(case), "solutions found in", time.time() - start, "sec.")

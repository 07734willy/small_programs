from collections import deque

try: input = raw_input  #Python 2.x compatibility
except NameError: pass

@profile
def count_matches(delta, wish_sizes, app_sizes):
    counter = 0
    for wish_size in wish_sizes:
        while app_sizes:
            if wish_size - delta <= app_sizes[0]:
                if wish_size + delta >= app_sizes[0]:
                    app_sizes.pop()
                    counter += 1
                break
            app_sizes.pop()
        else: break
    
    return counter

@profile
def main():
    _, _, delta = [int(x) for x in input().split()]
    wish_sizes =  [int(x) for x in input().split()]
    app_sizes =   [int(x) for x in input().split()]
    
    wish_sizes.sort()
    app_sizes = deque(sorted(app_sizes))

    matches = count_matches(delta, wish_sizes, app_sizes)
    print(matches)

if __name__ == "__main__":
    main()

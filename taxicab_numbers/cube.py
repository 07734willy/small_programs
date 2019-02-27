import heapq
import time

def main(n):
    heap = []
    heapq.heappush(heap, (0, (0, 0)))
    
    cube_pairs = []
    while heap:
        value, (a, b) = smallest = heapq.heappop(heap)
        
        if a != b:
            heapq.heappush(heap, (a ** 3 + (b + 1) ** 3, (a, b + 1)))
        if b == 0 and a <= n:
            heapq.heappush(heap, ((a + 1) ** 3, (a + 1, 0)))

        if cube_pairs and cube_pairs[0][0] != value:
            if len(cube_pairs) > 1:
                print(" == ".join(["{}**3 + {}**3".format(x, y) for _, (x, y) in cube_pairs]))
            cube_pairs = [smallest]
        else:
            cube_pairs.append(smallest)

if __name__ == "__main__":
    n = int(input())
    start = time.time()
    main(n)
    #print(time.time() - start)

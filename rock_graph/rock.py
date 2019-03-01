from bisect import bisect_right
from heapq import heappush, heappop

class Edge:
    # Left/Right index, Left/Right rock lists
    def __init__(self, lidx, ridx, left, right):
        self.lidx = lidx
        self.ridx = ridx
        self.left  = left
        self.right = right
        self.weight = (left[lidx][0] - right[ridx])**2 + left[lidx][1]

    # Used by heapq for ordering
    def __lt__(self, other):
        return self.weight < other.weight
    
    # Yield the next edge above/below the current
    def next_edge(self):
        # Assume edge below
        new_ridx = self.ridx - 1
        # If `j` is above `j-1`
        # -correct ridx to be the edge above instead
        if self.right[self.ridx] > self.left[self.lidx][0]:
            new_ridx += 2

        # If within the bounds of right_rocks, return
        if 0 <= new_ridx < len(self.right):
            return Edge(self.lidx, new_ridx, self.left, self.right)

    def get_right(self):
        return self.right[self.ridx]

    def get_left(self):
        return self.left[self.lidx][0]

# Find the min distance to each rock in `j`
# :left_rocks:  [(rock_row, weight), ...]
# :right_rocks: [rock_row, ...]
def min_jump(left_rocks, right_rocks):
    
    # Insert edges from each `j-1` to 2 edges in `j`
    # These "clamp" the min distance interval to each `j-1`
    heap = []
    for lidx in range(len(left_rocks)):
        ridx = bisect_right(right_rocks, lidx)
        
        # If these edges land within valid intervals, add them
        if 0 <= ridx < len(right_rocks):
            heappush(heap, Edge(lidx, ridx,   left_rocks, right_rocks))
        if 0 <= ridx + 1 < len(right_rocks):
            heappush(heap, Edge(lidx, ridx+1, left_rocks, right_rocks))

    unvisited = set(right_rocks)
    shortest = dict()

    # Find the shortest path to each `j` rock
    while unvisited:
        # Pop the min edge; get its `j` rock
        edge = heappop(heap)
        rock = edge.get_right()
        # If this is the shortest path to `j`
        if rock in unvisited:
            unvisited.remove(rock)
            print(unvisited)
            print(edge.get_left(), rock, edge.weight)
            shortest[rock] = edge.weight
            
            # Add a new edge to the queue
            # Visually next to (just above/below) the old edge,
            # from the same `j-1` rock
            next_edge = edge.next_edge()
            if next_edge:
                print("next", next_edge.get_right())
                heappush(heap, next_edge)
    return shortest

from random import randint
if __name__ == "__main__":
    #left = [(1,2),(4,39)]
    #right = [7,8,9]
    #print(min_jump(left, right))
    size = 10
    last = list(zip(set(randint(0,size) for _ in range(size)), list(randint(1, size) for _ in range(size))))

    for row_num in range(size):
        next_col = list(set(randint(0, size) for _ in range(size)))
        print(last[:10])
        print(next_col[:10])
        new = min_jump(last, next_col)
        last = zip(new.items())


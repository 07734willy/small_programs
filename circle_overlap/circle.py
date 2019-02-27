from itertools import combinations
from math import acos

class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def get_distance(self, circle):
        return ((self.x - circle.x) ** 2 + (self.y - circle.y) ** 2) ** 0.5

    def is_intersect(self, circle):
        return self.get_distance(circle) < self.r + circle.r

    def get_overlap_area(self, circle):
        if not is_intersect(circle): return 0
        dist = self.get_distance(circle)
        
        s = (self.r + circle.r + dist) / 2
        height = 2 * (s * (s-self.r) * (s-circle.r) * (s-dist)) ** 0.5 / d
        
        d1 = (self.r**2 - height**2) ** 0.5
        angle1 = acos(d1 / self.r)
        angle2 = acos((dist - d1) / circle.r)
        return angle1 * self.r**2 + angle2 * circle.r**2 - height * dist


if __name__ == "__main__":
    cir = [(1,3,0.4),(2,3,0.7),(3,3,0.9)]
    circles = [Circle(*params) for params in cir]

    for c1, c2 in combinations(circles, 2):
        pass

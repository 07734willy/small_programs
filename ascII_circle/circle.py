import math

def draw_circle(points, height, width):
    grid = []
    for _ in range(height * 2 + 1):
        grid.append([' '] * (width * 2 + 1))

    for i in range(0, points):
        theta = 2 * i * math.pi / points
        x = round(width + width * math.cos(theta), 5)
        y = round(height + height * math.sin(theta), 5)
        x = math.floor(x) if x < width else math.ceil(x)
        y = math.floor(y) if y < height else math.ceil(y)
        grid[y][x] = "#"

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    num, height, width = [int(x) for x in input().split(" ")]
    draw_circle(num, height, width)

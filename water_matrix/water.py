import numpy as np

def solve(matrix):
    neighbors = np.minimum(matrix,    np.roll(matrix,    2, axis=0))
    neighbors = np.minimum(neighbors, np.roll(neighbors, 2, axis=1))
    neighbors = np.roll(neighbors, (-1, -1), (0, 1))

    diff = np.clip(neighbors - matrix, a_min=0, a_max=None)
    return np.sum(diff[1:-1,1:-1])

def main():
    """
    matrix = [[2, 2, 2, 2],
              [2, 1, 2, 1],
              [2, 2, 2, 1]]
    """
    matrix = [[3, 3, 3, 3, 5, 3],
              [3, 0, 2, 3, 1, 3],
              [3, 1, 2, 3, 1, 3],
              [3, 3, 3, 1, 3, 3]]
    
    matrix = np.array(matrix)

    result = solve(matrix)
    print(result)


if __name__ == "__main__":
    main()

def find_path_dfs(maze):
    rows, cols = len(maze), len(maze[0])
    path = []
    visited = set()

    def dfs(x, y):
        if not (0 <= x < rows and 0 <= y < cols):
            return False
        if maze[x][y] == 0 or (x, y) in visited:
            return False
        path.append((x, y))
        visited.add((x, y))

        if (x, y) == (rows - 1, cols - 1):
            return True

        # Intentar moverse en todas las direcciones: abajo, derecha, arriba, izquierda
        if dfs(x + 1, y) or dfs(x, y + 1) or dfs(x - 1, y) or dfs(x, y - 1):
            return True

        path.pop()  # Retroceder si no funciona ese camino
        return False

    if dfs(0, 0):
        return mark_path(maze, path)
    return None  # No se encontró camino


def mark_path(maze, path):
    result = [['-' for _ in row] for row in maze]
    for x, y in path:
        result[x][y] = 'x'
    return result


def print_maze(solution):
    if solution:
        for row in solution:
            print(row)
    else:
        print("No path found.")


if __name__ == '__main__':
    mazes = [
        [[1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 0, 0, 1],
         [1, 1, 1, 1]],

        [[1, 1, 1, 0, 1],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 1, 1, 1, 1]],

        [[1, 1, 0, 1, 1, 0],
         [0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1],
         [0, 0, 1, 0, 0, 1]],

        [[1, 0, 1, 1, 1, 0, 1],
         [1, 0, 1, 0, 1, 0, 1],
         [1, 1, 1, 0, 1, 1, 1],
         [0, 0, 1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1, 1, 1],
         [1, 0, 0, 0, 0, 0, 1],
         [1, 1, 1, 1, 1, 1, 1]]
    ]

    for i, maze in enumerate(mazes, 1):
        print(f"\nMaze {i}  solution:")
        solution = find_path_dfs(maze)
        print_maze(solution)

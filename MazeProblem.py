from collections import deque

def find_path(maze):
    rows, cols = len(maze), len(maze[0])
    start = (0, 0)
    end = (rows - 1, cols - 1)

    if maze[0][0] == 0 or maze[end[0]][end[1]] == 0:
        return None  # No possible path if start or end are walls

    # Directions: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque()
    queue.append((start, [start]))  # (current position, path to current)

    visited = set()
    visited.add(start)

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return mark_path(maze, path)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < rows and 0 <= ny < cols and
                maze[nx][ny] == 1 and (nx, ny) not in visited):
                queue.append(((nx, ny), path + [(nx, ny)]))
                visited.add((nx, ny))

    return None  # No path found

def mark_path(maze, path):
    result = [['-' for _ in row] for row in maze]
    for x, y in path:
        result[x][y] = 'S'
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
        print(f"\nMaze {i} solution:")
        solution = find_path(maze)
        print_maze(solution)
